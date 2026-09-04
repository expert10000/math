#!/usr/bin/env python3
"""Volume VIII source-only pedagogy checks. Standard library; no release writes.

This is a conservative static TeX checker, not a TeX interpreter or a proof
checker. Dynamic inputs/references and conditional TeX are reported as limits.
A canonical PDF build and independent mathematical review remain separate gates.
"""
from __future__ import annotations
import collections
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable, Iterable

SCHEMA = 1
ENVS = ('exercise', 'problem', 'hint', 'solution')
ENV_RE = re.compile(r'\\(begin|end)\s*\{(' + '|'.join(ENVS) + r')\}')
LABEL_RE = re.compile(r'\\label\s*\{([^{}]+)\}')
REF_RE = re.compile(r'\\(?:[cC]ref|[cC]refrange|[aA]utoref|eqref|pageref|nameref|ref)\*?\s*\{([^{}]+)\}')
INPUT_RE = re.compile(r'\\(?:input|include)(?![A-Za-z@])\s*(?:\{([^{}]*)\}|([^\s{}%]+))')
PLACEHOLDER_RE = re.compile(r'^(?:Exercise|Problem)\s*\d+\s*[.?:!]?$', re.I)
GOAL_HEAD_RE = re.compile(r'\\(?:sub)*section\*?(?:\[[^\]]*\])?\s*\{([^{}]*(?:[Oo]utcomes|[Ll]earning [Gg]oals|[Ll]earning [Oo]bjectives)[^{}]*)\}')
GENERIC_RE = re.compile(r'^(?:Use|Apply|Recall|Review|Look|Think|Compare|Take|Count|Set)\b.{0,105}[.!]?$', re.S)
MARKER = 'VIII-PEDAGOGY-HINT-v1.1'

class AuditError(RuntimeError):
    pass


def git(repo: Path, *args: str, check: bool = True) -> bytes:
    p = subprocess.run(['git', '-C', str(repo), *args], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=False)
    if check and p.returncode:
        raise AuditError('git ' + ' '.join(args) + ': ' + p.stderr.decode('utf-8', 'replace').strip())
    return p.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def decode(data: bytes) -> str:
    # Retain a possible U+FEFF BOM. Normalization is only for cross-platform Git
    # comparisons. Actual patching below preserves the worktree's original EOLs.
    try:
        return data.decode('utf-8').replace('\r\n', '\n')
    except UnicodeDecodeError as exc:
        raise AuditError('Expected UTF-8 TeX source') from exc


def mask_tex(text: str) -> str:
    """Mask comments and common literal regions in source order, preserving offsets.

    A commented-out verbatim opener must not hide active source on later lines.
    This lexer deliberately does not attempt macro expansion or conditionals.
    """
    out = list(text)
    def blank(a: int, b: int) -> None:
        for j in range(a, b):
            if out[j] not in '\r\n':
                out[j] = ' '
    opaque = re.compile(r'\\begin\s*\{(verbatim\*?|Verbatim|lstlisting|minted|comment)\}')
    i = 0
    while i < len(text):
        if text[i] == '%':
            end = text.find('\n', i)
            end = len(text) if end < 0 else end
            blank(i, end)
            i = end
            continue
        if text[i] == '\\':
            m = opaque.match(text, i)
            if m:
                closing = re.search(r'\\end\s*\{' + re.escape(m.group(1)) + r'\}', text[m.end():])
                end = m.end() + closing.end() if closing else len(text)
                blank(i, end)
                i = end
                continue
            verb = re.match(r'\\verb\*?([^a-zA-Z\s])', text[i:])
            if verb:
                delimiter = verb.group(1)
                start = i + verb.end()
                end = text.find(delimiter, start)
                line_end = text.find('\n', start)
                if end >= 0 and (line_end < 0 or end < line_end):
                    blank(i, end + 1)
                    i = end + 1
                    continue
            # A control symbol, e.g. \% or \\, consumes its second character.
            # Control words do not contain a percent sign.
            if i + 1 < len(text) and not text[i + 1].isalpha():
                i += 2
                continue
        i += 1
    return ''.join(out)


@dataclass(frozen=True)
class Block:
    kind: str
    start: int
    body_start: int
    body_end: int
    end: int
    body: str
    labels: tuple[str, ...]


def blocks(text: str) -> list[Block]:
    masked = mask_tex(text)
    stack: list[tuple[str, re.Match[str]]] = []
    result: list[Block] = []
    for m in ENV_RE.finditer(masked):
        event, kind = m.groups()
        if event == 'begin':
            if stack:
                raise AuditError('Nested pedagogical environments are unsupported: ' + kind)
            stack.append((kind, m))
        else:
            if not stack or stack[-1][0] != kind:
                raise AuditError('Unmatched pedagogical environment end: ' + kind)
            _, begin = stack.pop()
            body = text[begin.end():m.start()]
            labels = tuple(LABEL_RE.findall(masked[begin.end():m.start()]))
            result.append(Block(kind, begin.start(), begin.end(), m.start(), m.end(), body, labels))
    if stack:
        raise AuditError('Unclosed pedagogical environment: ' + stack[-1][0])
    return result


def plain_body(body: str) -> str:
    body = LABEL_RE.sub('', mask_tex(body))
    body = re.sub(r'^\s*\[[^\]]*\]', '', body, count=1)
    return ' '.join(body.split())


def paired(text: str) -> tuple[list[dict], list[str]]:
    """Read actual statement -> optional hint -> solution order, not totals."""
    entries, errors = [], []
    pending = None
    for b in blocks(text):
        if b.kind in ('exercise', 'problem'):
            if pending is not None:
                errors.append('Missing solution before the next statement: ' + pending['id'])
                entries.append(pending)
            pending = {'id': b.labels[0] if b.labels else '(unlabelled at offset %d)' % b.start,
                       'kind': b.kind, 'statement': b, 'hint': None, 'solution': None}
        elif b.kind == 'hint':
            if pending is None:
                errors.append('Orphan hint at offset %d' % b.start)
            elif pending['hint'] is not None:
                errors.append('Duplicate hint for ' + pending['id'])
            else:
                pending['hint'] = b
        elif b.kind == 'solution':
            if pending is None:
                errors.append('Orphan solution at offset %d' % b.start)
            else:
                pending['solution'] = b
                if pending['kind'] == 'exercise' and pending['hint'] is None:
                    errors.append('Exercise without hint: ' + pending['id'])
                entries.append(pending)
                pending = None
    if pending is not None:
        errors.append('Missing terminal solution: ' + pending['id'])
        entries.append(pending)
    return entries, errors


def hint_body(original: str, row: dict, newline: str) -> str:
    addition = row['addition']
    if MARKER in original:
        raise AuditError('Refusing to enrich an already marked hint: ' + row['exercise_label'])
    if not addition.strip() or any(x in addition for x in ('\\begin{hint}', '\\end{hint}', '\\label{', '\\input{')):
        raise AuditError('Invalid curated addition: ' + row['exercise_label'])
    marker = '% ' + MARKER + ' ' + row['exercise_label'] + ' ' + row['mode']
    if row['mode'] == 'append':
        # Keep every original body character, even existing trailing whitespace.
        # A fresh newline also prevents a terminal source comment eating text.
        return original + newline + marker + newline + addition + newline
    if row['mode'] in ('replace_template', 'replace_misdirected_clue'):
        return newline + marker + newline + addition + newline
    raise AuditError('Unknown hint mode: ' + str(row['mode']))


def patch(data: bytes, rows: Iterable[dict]) -> bytes:
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError as exc:
        raise AuditError('Expected UTF-8 chapter') from exc
    eol = '\r\n' if '\r\n' in text else '\n'
    if eol == '\r\n' and '\n' in text.replace('\r\n', ''):
        raise AuditError('Mixed newline styles; normalize explicitly before this package')
    if '\r' in text.replace('\r\n', ''):
        raise AuditError('Unsupported lone CR newline')
    entries, errors = paired(text)
    if errors:
        raise AuditError('; '.join(errors))
    by_label = {}
    for entry in entries:
        for label in entry['statement'].labels:
            if label in by_label:
                raise AuditError('Duplicate statement label: ' + label)
            by_label[label] = entry
    replacements, seen = [], set()
    for row in rows:
        label = row['exercise_label']
        if label in seen:
            raise AuditError('Duplicate bank label: ' + label)
        seen.add(label)
        entry = by_label.get(label)
        if entry is None or entry['kind'] != 'exercise' or entry['hint'] is None:
            raise AuditError('Expected labelled exercise with an inline hint: ' + label)
        h = entry['hint']
        replacements.append((h.body_start, h.body_end, hint_body(h.body, row, eol)))
    for a, b, value in sorted(replacements, reverse=True):
        text = text[:a] + value + text[b:]
    return text.encode('utf-8')


class Source:
    def __init__(self, repo: Path, ref: str | None = None, overlay: dict[str, bytes] | None = None):
        self.repo, self.ref, self.overlay = repo, ref, overlay or {}
        self.cache: dict[str, bytes | None] = {}

    def get(self, path: str) -> bytes | None:
        if path in self.overlay:
            return self.overlay[path]
        if path not in self.cache:
            if self.ref:
                p = subprocess.run(['git', '-C', str(self.repo), 'show', self.ref + ':' + path],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.cache[path] = p.stdout if p.returncode == 0 else None
            else:
                target = self.repo / path
                self.cache[path] = target.read_bytes() if target.is_file() else None
        return self.cache[path]


class Graph:
    def __init__(self, source: Source, entry: str, document_dir: str | None = None):
        self.source, self.entry = source, entry
        self.files: dict[str, str] = {}
        self.occurrences: list[str] = []
        self.issues: list[str] = []
        self.limits: list[str] = []
        self.document_dir = document_dir or str(PurePosixPath(entry).parent)
        self.text = self.expand(entry, ())

    @staticmethod
    def clean(path: PurePosixPath) -> str | None:
        parts: list[str] = []
        for p in path.parts:
            if p in ('', '.'):
                continue
            if p == '..':
                if not parts:
                    return None
                parts.pop()
            elif p == '/' or ':' in p:
                return None
            else:
                parts.append(p)
        return '/'.join(parts)

    def resolve(self, current: str, token: str) -> str | None:
        names = [token] if PurePosixPath(token).suffix else [token + '.tex', token]
        # TeX normally resolves relative to its build working directory. The
        # other candidates are conservative fallbacks and are reported as limits.
        bases = [self.document_dir, str(PurePosixPath(current).parent), '.']
        candidates = []
        for base in bases:
            for name in names:
                c = self.clean(PurePosixPath(base) / name)
                if c and c not in candidates:
                    candidates.append(c)
        for c in candidates:
            if self.source.get(c) is not None:
                ordinary = [self.clean(PurePosixPath(self.document_dir) / n) for n in names]
                if c not in ordinary:
                    self.limits.append('Non-document-directory include resolution requires build verification: ' + current + ' -> ' + c)
                return c
        return None

    def expand(self, path: str, stack: tuple[str, ...]) -> str:
        if path in stack:
            self.issues.append('Input cycle: ' + ' -> '.join(stack + (path,)))
            return ''
        data = self.source.get(path)
        if data is None:
            self.issues.append('Missing source: ' + path)
            return ''
        text = decode(data)
        self.files[path] = sha256(text.encode('utf-8'))
        self.occurrences.append(path)
        masked = mask_tex(text)
        if re.search(r'\\(?:if[a-zA-Z@]*|else|fi|includeonly)(?![A-Za-z@])', masked):
            self.limits.append('Conditional TeX requires build verification: ' + path)
        output, pos = [], 0
        for m in INPUT_RE.finditer(masked):
            output.append(text[pos:m.start()])
            token = (m.group(1) if m.group(1) is not None else m.group(2)).strip()
            if not token or any(c in token for c in ('#', '\\', '$')):
                self.limits.append('Dynamic include not expanded: ' + path + ': ' + token)
                output.append('\n')
            else:
                child = self.resolve(path, token)
                if child is None:
                    self.issues.append('Unresolved include: ' + path + ': ' + token)
                else:
                    output.append('\n' + self.expand(child, stack + (path,)) + '\n')
            pos = m.end()
        output.append(text[pos:])
        return ''.join(output)


def goal_inventory(text: str) -> dict:
    masked = mask_tex(text)
    matches = list(GOAL_HEAD_RE.finditer(masked))
    sections = []
    for m in matches:
        end = re.search(r'\\(?:sub)*section\*?(?:\[[^\]]*\])?\s*\{', masked[m.end():])
        endpos = m.end() + end.start() if end else len(text)
        body = text[m.end():endpos]
        # A goal list can be followed by theorem/exercise text before the next
        # section. Do not let action verbs in that later text certify the goals.
        list_end = re.search(r'\\end\s*\{(?:itemize|enumerate)\}', mask_tex(body))
        if list_end:
            body = body[:list_end.start()]
        items = re.split(r'\\item(?:\[[^\]]*\])?', mask_tex(body))[1:]
        measurable = r'\b(?:prove|compute|construct|verify|derive|determine|classify|compare|identify|explain|distinguish|apply|evaluate|calculate|state|define|show|analyze|analyse)\b'
        sections.append({'heading': m.group(1), 'body_sha256': sha256(body.encode('utf-8')),
                         'item_count': len(items),
                         'items_without_recognized_action_verb': [plain_body(x) for x in items if not re.search(measurable, x, re.I)]})
    return {'recognized_goal_sections': sections,
            'detection_note': 'Heading/verb heuristic; absence is a review flag, not proof that no outcome appears anywhere.'}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8-sig'))


def bank_rows(bank: dict) -> dict[str, list[dict]]:
    return {c['path']: c['hints'] for c in bank['chapters']}


def source_audit(repo: Path, plan: dict, stage: int, banks: list[dict], findings: dict,
                 overlay: dict[str, bytes] | None = None) -> dict:
    if stage not in (1, 2, 3):
        raise AuditError('Stage must be 1, 2, or 3')
    base = plan['base_commit']
    before, after = Source(repo, base), Source(repo, overlay=overlay)
    expected_rows: dict[str, list[dict]] = {}
    for bank in banks:
        if bank['base_commit'] != base:
            raise AuditError('Bank and plan baselines differ')
        for c in bank['chapters']:
            number = int(c['chapter_code'].split('/')[1])
            if stage >= (2 if number <= 17 else 3):
                if c['path'] in expected_rows:
                    raise AuditError('Duplicate chapter in bank')
                expected_rows[c['path']] = c['hints']
    expected_hint_count = {1: 0, 2: 408, 3: 840}[stage]
    structural, review, chapters, totals = [], [], [], collections.Counter()
    if sum(len(x) for x in expected_rows.values()) != expected_hint_count:
        structural.append('Expected curated bank coverage is not present for this stage')
    graph_base = Graph(before, plan['entry_point'])
    graph = Graph(after, plan['entry_point'])
    structural += graph_base.issues + graph.issues
    if graph.files.keys() != graph_base.files.keys() or graph.occurrences != graph_base.occurrences:
        structural.append('Active source graph differs from the pinned baseline')
    chapter_paths = [c['path'] for c in plan['chapters']]
    if len(chapter_paths) != 35 or len(set(chapter_paths)) != 35:
        structural.append('Plan must contain exactly 35 distinct canonical chapters')
    for path in chapter_paths:
        if graph.occurrences.count(path) != 1:
            structural.append('Canonical chapter is not included exactly once: ' + path)
    for path in graph.files:
        original, current = before.get(path), after.get(path)
        if original is None or current is None:
            continue
        rows = expected_rows.get(path, [])
        try:
            expected = patch(original, rows) if rows else original
            if decode(expected) != decode(current):
                structural.append('Protected source or expected hint content differs: ' + path)
        except AuditError as exc:
            structural.append(path + ': ' + str(exc))
    for meta in plan['chapters']:
        path = meta['path']
        data = before.get(path)
        if data is not None and meta.get('source_blob') and git_blob_sha(data) != meta['source_blob']:
            structural.append('Pinned source blob differs from inspected source: ' + path)
        before_ch = Graph(before, path, graph_base.document_dir)
        after_ch = Graph(after, path, graph.document_dir)
        structural += before_ch.issues + after_ch.issues
        try:
            original_entries, original_errors = paired(before_ch.text)
            entries, errors = paired(after_ch.text)
        except AuditError as exc:
            structural.append(path + ': ' + str(exc))
            continue
        structural += [meta['chapter_code'] + ': ' + x for x in errors]
        before_counts = collections.Counter(b.kind for b in blocks(before_ch.text))
        counts = collections.Counter(b.kind for b in blocks(after_ch.text))
        if before_counts != counts:
            structural.append('Environment counts changed: ' + path)
        totals.update(counts)
        missing_statements = [e['id'] for e in entries if PLACEHOLDER_RE.fullmatch(plain_body(e['statement'].body))]
        blank_solutions = [e['id'] for e in entries if e['solution'] and not plain_body(e['solution'].body)]
        goals = goal_inventory(after_ch.text)
        if missing_statements:
            review.append({'kind': 'placeholder_statements', 'chapter': meta['chapter_code'], 'labels': missing_statements})
        if blank_solutions:
            review.append({'kind': 'empty_solutions', 'chapter': meta['chapter_code'], 'labels': blank_solutions})
        if not goals['recognized_goal_sections']:
            review.append({'kind': 'outcome_heading_not_detected', 'chapter': meta['chapter_code']})
        for section in goals['recognized_goal_sections']:
            if section['items_without_recognized_action_verb']:
                review.append({'kind': 'outcome_action_verb_review', 'chapter': meta['chapter_code'], 'heading': section['heading']})
        hint_texts = [plain_body(e['hint'].body) for e in entries if e['hint']]
        counts_hint = collections.Counter(hint_texts)
        repeat_hints = [{'text': h, 'count': n} for h,n in counts_hint.items() if n > 1]
        generic_only = [e['id'] for e in entries if e['hint'] and MARKER not in e['hint'].body
                        and GENERIC_RE.fullmatch(plain_body(e['hint'].body))]
        if repeat_hints:
            review.append({'kind': 'exact_repeated_hints', 'chapter': meta['chapter_code'], 'groups': repeat_hints})
        if generic_only:
            review.append({'kind': 'short_generic_hint_candidates', 'chapter': meta['chapter_code'], 'labels': generic_only})
        chapters.append({'chapter': meta['chapter_code'], 'path': path,
                         'counts_from_active_source': dict(counts),
                         'baseline_counts_from_active_source': dict(before_counts),
                         'pairing_failures': errors, 'baseline_pairing_failures': original_errors,
                         'placeholder_statements': missing_statements,
                         'hints_enriched': len(expected_rows.get(path, [])),
                         'outcome_inventory': goals,
                         'hint_actionability_basis': 'curated individual mathematical additions; not inferred from marker or length'})
    labels = LABEL_RE.findall(mask_tex(graph.text))
    dynamic_labels = [x for x in labels if '#' in x or '\\' in x]
    actual_labels = [x.strip() for x in labels if x not in dynamic_labels]
    label_counts = collections.Counter(actual_labels)
    duplicates = sorted(x for x,n in label_counts.items() if n > 1)
    references, dynamic_refs = [], []
    masked_full = mask_tex(graph.text)
    for m in REF_RE.finditer(masked_full):
        token = m.group(1)
        if any(x in token for x in ('#', '\\', '$')):
            dynamic_refs.append(token)
        else:
            references.extend(x.strip() for x in token.split(','))
        # cleveref range macros have two braced endpoint labels.
        if re.match(r'\\[cC]refrange', m.group(0)):
            second = re.match(r'\s*\{([^{}]+)\}', masked_full[m.end():])
            if second:
                token2 = second.group(1)
                if '#' in token2 or '\\' in token2:
                    dynamic_refs.append(token2)
                else:
                    references.append(token2.strip())
    missing_refs = sorted(set(references) - set(actual_labels))
    if duplicates:
        structural.append('Duplicate active labels: ' + ', '.join(duplicates))
    if missing_refs:
        structural.append('Unresolved static references: ' + ', '.join(missing_refs))
    relevant_findings = []
    for finding in findings.get('findings', []):
        original = before.get(finding['path'])
        current = after.get(finding['path'])
        # Findings are never silently closed by this preservation-only package.
        f = dict(finding)
        f['status'] = 'OPEN_PROTECTED_CONTENT' if original is not None and current is not None else 'SOURCE_NOT_AVAILABLE'
        relevant_findings.append(f)
    limitations = sorted(set(graph.limits + graph_base.limits))
    if dynamic_labels or dynamic_refs:
        limitations.append('Dynamic labels or references require the actual TeX build')
    structural = list(dict.fromkeys(structural))
    report = {'schema_version': SCHEMA, 'package_id': plan['package_id'], 'base_commit': base,
              'working_parent_commit': git(repo, 'rev-parse', 'HEAD').decode().strip(),
              'stage': stage, 'scope': 'Volume VIII only; source checks, no freeze',
              'structural_source_status': 'PASS' if not structural else 'FAIL',
              'pedagogy_readiness': 'HOLD',
              'canonical_pdf_build': 'NOT_RUN_BY_THIS_AUDIT',
              'series_I_VIII_audit': 'NOT_RUN', 'freeze_executed': False,
              'structural_failures': structural, 'review_findings': review,
              'protected_mathematical_findings': relevant_findings,
              'counts_from_active_source': dict(totals), 'curated_hint_coverage': sum(len(v) for v in expected_rows.values()),
              'canonical_chapters_in_plan': len(chapter_paths), 'chapters': chapters,
              'active_input_occurrences': graph.occurrences,
              'active_source_normalized_sha256': graph.files,
              'baseline_active_source_normalized_sha256': graph_base.files,
              'duplicate_labels': duplicates, 'unresolved_static_references': missing_refs,
              'dynamic_reference_candidates': dynamic_refs, 'static_analysis_limits': limitations,
              'release_note': 'Source PASS does not certify mathematical correctness, PDF references, goal sufficiency, or release readiness. Known protected findings and unrun build/review gates keep readiness on HOLD.'}
    return report


def report_markdown(report: dict) -> str:
    total_placeholder = sum(len(c['placeholder_statements']) for c in report['chapters'])
    counts = report['counts_from_active_source']
    lines = ['# Volume VIII pedagogy — stage %d' % report['stage'], '',
             '- Pinned base: `' + report['base_commit'] + '`.',
             '- Structural source checks: **' + report['structural_source_status'] + '**.',
             '- Pedagogy readiness: **HOLD** (not a release/freeze audit).',
             '- Canonical PDF build: **NOT RUN by this audit**.',
             '- I–VIII audit, release hashes, inventory refresh, tags and freeze: **NOT RUN**.', '',
             '## Direct source counts', '',
             '| Chapters | Problems | Exercises | Hints | Solutions | Curated hints applied |',
             '|---:|---:|---:|---:|---:|---:|',
             '| %d | %d | %d | %d | %d | %d |' % (len(report['chapters']), counts.get('problem',0), counts.get('exercise',0), counts.get('hint',0), counts.get('solution',0), report['curated_hint_coverage']), '',
             'These counts were computed from the active TeX input graph, not copied from a release ledger.', '',
             '## Blocking/review findings', '',
             'Unresolved placeholder exercise/problem statements: **%d**.' % total_placeholder,
             'Chapters without a recognized outcome heading: **%d**. This is a detection flag requiring review, not a claim that no learning outcome exists elsewhere.' % sum(not c['outcome_inventory']['recognized_goal_sections'] for c in report['chapters']), '']
    for f in report['protected_mathematical_findings']:
        lines.append('**%s — %s.** %s Source: `%s`, %s. Status: `%s`.' % (f['id'], f['title'], f['explanation'], f['path'], f['location'], f['status']))
        lines.append('')
    lines += ['## Structural failures', ''] + (['- '+x for x in report['structural_failures']] or ['None detected by the static source checks.'])
    lines += ['', '## Chapter inventory', '', '| Chapter | Problems | Exercises | Hints | Solutions | Enriched | Placeholders |', '|---|---:|---:|---:|---:|---:|---:|']
    for c in report['chapters']:
        x=c['counts_from_active_source']
        lines.append('| %s | %d | %d | %d | %d | %d | %d |' % (c['chapter'],x.get('problem',0),x.get('exercise',0),x.get('hint',0),x.get('solution',0),c['hints_enriched'],len(c['placeholder_statements'])))
    lines += ['', '## Verification boundary', '', report['release_note'], '', 'The full JSON lists exact placeholder labels, goal evidence, pairing failures, input occurrences, static reference results and source hashes. These hashes are preservation evidence, not refreshed PDF/release hashes.', '', 'Static-analysis limits:', '']
    lines += ['- '+x for x in report['static_analysis_limits']] or ['No additional dynamic-TeX limits detected; a real build is still required.']
    return '\n'.join(lines)+'\n'
