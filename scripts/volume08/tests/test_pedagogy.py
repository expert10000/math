#!/usr/bin/env python3
"""Unit tests for the preservation patcher, static scanner, and curated bank.

Run with: python -B -m unittest discover -s scripts/volume08/tests -v
These are tool tests, not a canonical-volume build or a full mathematical audit.
"""
import collections
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from pedagogy_core import (AuditError, Graph, Source, blocks, decode, goal_inventory,
                           mask_tex, paired, patch, plain_body, MARKER)

SAMPLE=r'''\chapter{Example}\label{ch:sample}
\section{Learning outcomes}
\begin{itemize}\item Compute a quotient group.\end{itemize}
\begin{theorem}\label{thm:keep}This theorem is protected.\end{theorem}
\begin{exercise}\label{exr:sample}Compute the quotient.\end{exercise}
\begin{hint}
Use the kernel and image.
\end{hint}
\begin{solution}The protected solution has a label \label{sol:keep}.\end{solution}
\begin{problem}[Dossier]\label{prob:keep}State a theorem.\end{problem}
\begin{solution}This solution is also protected.\end{solution}
'''
ROW={'exercise_label':'exr:sample','addition':r'Choose \(z\in\ker d_n\), then identify representatives differing by \(d_{n+1}c\).','mode':'append'}

def protected(text):
    spans=[b for b in blocks(text) if b.kind=='hint']
    for b in reversed(spans): text=text[:b.body_start]+'<HINT>'+text[b.body_end:]
    return text

class PatcherTests(unittest.TestCase):
    def test_append_preserves_every_nonhint_character(self):
        after=patch(SAMPLE.encode(),[ROW]).decode()
        self.assertEqual(protected(after),protected(SAMPLE))
        self.assertIn('Use the kernel and image.',after)
        self.assertIn(MARKER,after)
    def test_bom_and_crlf_preserved(self):
        original=('\ufeff'+SAMPLE).replace('\n','\r\n').encode()
        after=patch(original,[ROW])
        self.assertTrue(after.startswith(b'\xef\xbb\xbf'))
        self.assertNotIn(b'\n',after.replace(b'\r\n',b''))
        self.assertEqual(protected(after.decode()),protected(original.decode()))
    def test_mixed_line_endings_rejected(self):
        with self.assertRaises(AuditError): patch((SAMPLE.replace('\n','\r\n',1)).encode(),[ROW])
    def test_duplicate_bank_label_rejected(self):
        with self.assertRaises(AuditError): patch(SAMPLE.encode(),[ROW,ROW])
    def test_missing_label_rejected(self):
        with self.assertRaises(AuditError): patch(SAMPLE.encode(),[dict(ROW,exercise_label='missing')])
    def test_reapplication_rejected(self):
        with self.assertRaises(AuditError): patch(patch(SAMPLE.encode(),[ROW]),[ROW])
    def test_source_injection_rejected(self):
        with self.assertRaises(AuditError): patch(SAMPLE.encode(),[dict(ROW,addition=r'\input{unsafe}')])
    def test_replace_template_only_changes_hint(self):
        after=patch(SAMPLE.encode(),[dict(ROW,mode='replace_template')]).decode()
        self.assertEqual(protected(after),protected(SAMPLE))
        self.assertNotIn('Use the kernel and image.',after)
    def test_replace_misdirected_only_changes_hint(self):
        after=patch(SAMPLE.encode(),[dict(ROW,mode='replace_misdirected_clue')]).decode()
        self.assertEqual(protected(after),protected(SAMPLE))
    def test_inline_hint_and_terminal_comment(self):
        source=SAMPLE.replace('\nUse the kernel and image.\n',r'Use the kernel. % comment'+'\n')
        after=patch(source.encode(),[ROW]).decode()
        self.assertIn(ROW['addition'],plain_body(next(b.body for b in blocks(after) if b.kind=='hint')))
    def test_pairing_reads_order_not_just_counts(self):
        source=SAMPLE.replace(r'\begin{solution}The protected solution',r'\begin{hint}Extra\end{hint}\begin{solution}The protected solution')
        self.assertTrue(any('Duplicate hint' in x for x in paired(source)[1]))
    def test_orphan_solution_rejected(self):
        entries,errors=paired(r'\begin{solution}Orphan\end{solution}'+SAMPLE)
        self.assertTrue(any('Orphan solution' in x for x in errors))
    def test_missing_solution_rejected(self):
        source=r'\begin{exercise}\label{x}Question\end{exercise}\begin{hint}H\end{hint}'
        self.assertTrue(any('Missing terminal solution' in x for x in paired(source)[1]))
    def test_nested_target_environment_rejected(self):
        with self.assertRaises(AuditError): blocks(r'\begin{exercise}\begin{hint}h\end{hint}\end{exercise}')
    def test_unlabelled_dossier_is_valid(self):
        entries,errors=paired(r'\begin{problem}Question\end{problem}\begin{solution}Answer\end{solution}')
        self.assertEqual(errors,[]); self.assertEqual(len(entries),1)
    def test_duplicate_source_label_rejected(self):
        source=SAMPLE+SAMPLE.replace('ch:sample','ch:other')
        with self.assertRaises(AuditError): patch(source.encode(),[ROW])
    def test_empty_patch_preserves_bytes(self): self.assertEqual(patch(SAMPLE.encode(),[]),SAMPLE.encode())

class ScannerTests(unittest.TestCase):
    def test_comments_ignore_fake_environments(self):
        source='% '+r'\begin{exercise}'+'\n'+SAMPLE
        self.assertEqual(len(blocks(source)),len(blocks(SAMPLE)))
    def test_commented_verbatim_opener_does_not_hide_active_source(self):
        source='% '+r'\begin{verbatim}'+'\n'+SAMPLE+'\n% '+r'\end{verbatim}'
        self.assertEqual(len(blocks(source)),len(blocks(SAMPLE)))
    def test_verbatim_is_opaque(self):
        self.assertEqual(blocks(r'\begin{verbatim}\begin{exercise}fake\end{verbatim}'),[])
    def test_verb_is_opaque(self): self.assertEqual(blocks(r'\verb|\begin{exercise}|'),[])
    def test_escaped_percent_retained(self): self.assertEqual(mask_tex(r'\% real'),r'\% real')
    def test_double_slash_does_not_escape_comment(self):
        self.assertNotIn('hidden',mask_tex(r'\\% hidden'))
    def test_mask_preserves_length_and_newline_positions(self):
        text='% hi\n'+r'\verb|fake|'+'\nrest'
        masked=mask_tex(text);self.assertEqual(len(text),len(masked))
        self.assertEqual([i for i,c in enumerate(text) if c=='\n'],[i for i,c in enumerate(masked) if c=='\n'])
    def test_outcomes_detected_without_rewriting(self):
        inv=goal_inventory(SAMPLE)
        self.assertEqual(inv['recognized_goal_sections'][0]['item_count'],1)
        self.assertEqual(inv['recognized_goal_sections'][0]['items_without_recognized_action_verb'],[])
    def test_nonmeasurable_outcome_is_review_flag(self):
        inv=goal_inventory(SAMPLE.replace('Compute a quotient group.','Appreciate the subject.'))
        self.assertEqual(len(inv['recognized_goal_sections'][0]['items_without_recognized_action_verb']),1)
    def test_input_graph_missing_and_cycle(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); (root/'book.tex').write_text(r'\input{a}\input{missing}')
            (root/'a.tex').write_text(r'\input{book}')
            g=Graph(Source(root),'book.tex')
            self.assertTrue(any('cycle' in x for x in g.issues))
            self.assertTrue(any('Unresolved' in x for x in g.issues))
    def test_commented_input_is_not_followed(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'book.tex').write_text('% '+r'\input{missing}')
            self.assertEqual(Graph(Source(root),'book.tex').issues,[])
    def test_document_directory_resolution(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'chapters').mkdir();(root/'parts').mkdir()
            (root/'chapters/ch.tex').write_text(r'\input{parts/piece}')
            (root/'parts/piece.tex').write_text('Piece')
            g=Graph(Source(root),'chapters/ch.tex',document_dir='.')
            self.assertIn('Piece',g.text);self.assertEqual(g.issues,[])
    def test_path_escape_rejected(self): self.assertIsNone(Graph.clean(Path('../../etc/passwd')))

class BankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        names=[ROOT/'hints_01_17.json',ROOT/'hints_18_35.json']
        if not all(x.exists() for x in names): raise unittest.SkipTest('Complete bank is installed only after stage 3')
        cls.banks=[json.loads(p.read_text()) for p in names]
        cls.chapters=[c for b in cls.banks for c in b['chapters']]
        cls.rows=[r for c in cls.chapters for r in c['hints']]
    def test_counts_and_unique_labels(self):
        self.assertEqual([sum(len(c['hints']) for c in b['chapters']) for b in self.banks],[408,432])
        self.assertEqual(len(self.chapters),35)
        self.assertEqual(len({r['exercise_label'] for r in self.rows}),840)
    def test_no_duplicate_complete_additions(self): self.assertEqual(len({r['addition'] for r in self.rows}),840)
    def test_preservation_modes(self):
        self.assertEqual(collections.Counter(r['mode'] for r in self.rows),{'append':623,'replace_template':216,'replace_misdirected_clue':1})
    def test_missing_statement_alignment_not_claimed(self):
        marked=[c for c in self.chapters if c['alignment_basis']=='existing_solution_missing_exercise_statement']
        self.assertEqual([c['chapter_code'] for c in marked],[f'VIII/{n:02d}' for n in range(22,31)])
    def test_every_chapter_has_24_exact_labels(self):
        for n,c in enumerate(self.chapters,1):
            self.assertEqual([r['exercise_label'] for r in c['hints']],[f'exr:viii{n:02d}-{j:02d}' for j in range(1,25)])
    def test_tex_delimiters_and_braces(self):
        for r in self.rows:
            s=r['addition']; self.assertEqual(s.count(r'\('),s.count(r'\)'),r['exercise_label'])
            self.assertEqual(s.count(r'\['),s.count(r'\]'),r['exercise_label'])
            depth=0
            for m in re.finditer(r'(?<!\\)[{}]',s):
                depth += 1 if m.group()=='{' else -1
                self.assertGreaterEqual(depth,0,r['exercise_label'])
            self.assertEqual(depth,0,r['exercise_label'])
    def test_bank_has_no_pedagogical_environment_injection(self):
        for r in self.rows:
            self.assertNotRegex(r['addition'],r'\\(?:begin|end)\{(?:exercise|problem|solution|hint)\}|\\label\{|\\input\{')

class MathematicalSanityTests(unittest.TestCase):
    def test_free_word_reduces_to_ab(self):
        stack=[]
        for letter in ['a','b','A','a','B','b']:
            if stack and stack[-1]==letter.swapcase(): stack.pop()
            else: stack.append(letter)
        self.assertEqual(''.join(stack),'ab')
    def test_torus_determinant_trace_identity(self):
        for a in range(-2,3):
            for b in range(-2,3):
                for c in range(-2,3):
                    for d in range(-2,3):
                        self.assertEqual((1-a)*(1-d)-b*c,1-(a+d)+(a*d-b*c))
    def test_cyclic_tor_kernel_size(self):
        import math
        for m in range(1,13):
            for n in range(1,13):
                self.assertEqual(sum((m*x)%n==0 for x in range(n)),math.gcd(m,n))
    def test_hyperbolic_parity_and_signature_contrast(self):
        for x in range(-5,6):
            for y in range(-5,6): self.assertEqual((2*x*y)%2,0)
        self.assertEqual((1*1-0*0)%2,1)

if __name__=='__main__': unittest.main(verbosity=2)
