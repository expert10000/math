param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "",

    [Parameter(Mandatory=$false)]
    [string]$ExpectedStatus = "",

    [Parameter(Mandatory=$false)]
    [string]$ExpectedNextAction = ""
)

$ErrorActionPreference = "Stop"

function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory=$true)][string]$Path,
        [Parameter(Mandatory=$true)][string]$Text
    )
    $enc = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $enc)
}

if ([string]::IsNullOrWhiteSpace($Repo)) {
    $Repo = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
} else {
    $Repo = (Resolve-Path $Repo).Path
}

$volRel = "books/vol07_differential_geometry"
$vol = Join-Path $Repo $volRel
$statusPath = Join-Path $Repo "editorial/CHAPTER_STATUS.tsv"
$bookPath = Join-Path $vol "book.tex"
$reportMd = Join-Path $Repo "editorial/VOLUME_VII_CORPUS_AUDIT.md"
$reportJson = Join-Path $Repo "editorial/VOLUME_VII_CORPUS_AUDIT.json"

foreach ($requiredPath in @($vol, $statusPath, $bookPath)) {
    if (-not (Test-Path -LiteralPath $requiredPath)) {
        throw "Required Volume VII audit input is missing: $requiredPath"
    }
}

$rows = Import-Csv -LiteralPath $statusPath -Delimiter "`t"
$viiRows = @($rows | Where-Object { $_.volume -eq "VII" } | Sort-Object chapter_code)
$issues = @()
$warnings = @()

if ($viiRows.Count -ne 42) {
    $issues += "CHAPTER_STATUS.tsv must contain exactly 42 Volume VII rows; found $($viiRows.Count)."
}

$expectedCodes = @(1..42 | ForEach-Object { "VII/{0:D2}" -f $_ })
$actualCodes = @($viiRows | ForEach-Object { $_.chapter_code })

foreach ($code in $expectedCodes) {
    if ($actualCodes -notcontains $code) {
        $issues += "Missing chapter-status row: $code"
    }
}
foreach ($code in $actualCodes) {
    if ($expectedCodes -notcontains $code) {
        $issues += "Unexpected Volume VII chapter-status row: $code"
    }
}

if (-not [string]::IsNullOrWhiteSpace($ExpectedStatus)) {
    foreach ($row in $viiRows) {
        if ($row.status -ne $ExpectedStatus) {
            $issues += "$($row.chapter_code) status is '$($row.status)' but expected '$ExpectedStatus'."
        }
    }
}
if (-not [string]::IsNullOrWhiteSpace($ExpectedNextAction)) {
    foreach ($row in $viiRows) {
        if ($row.next_action -ne $ExpectedNextAction) {
            $issues += "$($row.chapter_code) next_action is '$($row.next_action)' but expected '$ExpectedNextAction'."
        }
    }
}

$bookText = [System.IO.File]::ReadAllText($bookPath)
$includeMatches = [regex]::Matches($bookText, '(?m)^[ \t]*\\include\{([^}]+)\}')
$activeIncludes = @($includeMatches | ForEach-Object { $_.Groups[1].Value })

$allLabels = @()
$labelRecords = @()
$allRefs = @()
$chapterSummaries = @()

foreach ($row in $viiRows) {
    $canonicalRel = $row.canonical_path.Replace("/", [System.IO.Path]::DirectorySeparatorChar)
    $chapterPath = Join-Path $Repo $canonicalRel

    if (-not (Test-Path -LiteralPath $chapterPath)) {
        $issues += "$($row.chapter_code) canonical file is missing: $($row.canonical_path)"
        continue
    }

    $fullChapter = (Resolve-Path -LiteralPath $chapterPath).Path
    if ($fullChapter.IndexOf($vol, [System.StringComparison]::OrdinalIgnoreCase) -ne 0) {
        $issues += "$($row.chapter_code) canonical path is outside Volume VII: $($row.canonical_path)"
    }

    $chapterText = [System.IO.File]::ReadAllText($chapterPath)
    $chapterCount = ([regex]::Matches($chapterText, '\\chapter\{')).Count
    if ($chapterCount -ne 1) {
        $issues += "$($row.chapter_code) must contain exactly one \chapter{...}; found $chapterCount."
    }

    $chapterNumber = [int]($row.chapter_code.Split("/")[1])
    $chapterLabelPrefix = "ch:vii{0:D2}" -f $chapterNumber

    $labelMatches = [regex]::Matches($chapterText, '\\label\{([^}]+)\}')
    $labels = @($labelMatches | ForEach-Object { $_.Groups[1].Value })
    $chapterLabels = @($labels | Where-Object {
        $_ -ceq $chapterLabelPrefix -or $_.StartsWith($chapterLabelPrefix + "-", [System.StringComparison]::Ordinal)
    })

    if ($chapterLabels.Count -ne 1) {
        $issues += "$($row.chapter_code) must have exactly one chapter label beginning '$chapterLabelPrefix'; found $($chapterLabels.Count)."
    }

    foreach ($label in $labels) {
        $allLabels += $label
        $labelRecords += [pscustomobject]@{
            label = $label
            owner = $row.chapter_code
        }
    }

    $refMatches = [regex]::Matches($chapterText, '\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^}]+)\}')
    foreach ($m in $refMatches) {
        $allRefs += $m.Groups[1].Value
    }

    $exerciseCount = ([regex]::Matches($chapterText, '\\begin\{exercise\}')).Count
    $hintCount = ([regex]::Matches($chapterText, '\\begin\{hint\}')).Count
    $problemCount = ([regex]::Matches($chapterText, '\\begin\{problem\}')).Count
    $solutionCount = ([regex]::Matches($chapterText, '\\begin\{solution\}')).Count
    $expectedSolutions = $exerciseCount + $problemCount

    if ($exerciseCount -lt 1) {
        $issues += "$($row.chapter_code) has no exercise environment."
    }
    if ($hintCount -ne $exerciseCount) {
        $issues += "$($row.chapter_code) has $exerciseCount exercises but $hintCount hints."
    }
    if ($solutionCount -ne $expectedSolutions) {
        $issues += "$($row.chapter_code) has $exerciseCount exercises and $problemCount solved problems, so expected $expectedSolutions solution environments but found $solutionCount."
    }

    $placeholderMatches = [regex]::Matches(
        $chapterText,
        '(?im)\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b|\\lipsum\b'
    )
    if ($placeholderMatches.Count -gt 0) {
        $issues += "$($row.chapter_code) contains TODO/FIXME/TBD/PLACEHOLDER/lipsum markers."
    }

    $relativeToVol = $row.canonical_path.Substring(($volRel + "/").Length)
    $includeTarget = $relativeToVol -replace '\.tex$', ''
    if ($activeIncludes -notcontains $includeTarget) {
        $issues += "$($row.chapter_code) is not actively included by Volume VII book.tex: $includeTarget"
    }

    $chapterSummaries += [pscustomobject]@{
        code = $row.chapter_code
        title = $row.chapter_title
        status = $row.status
        next_action = $row.next_action
        mapped_rules = [int]$row.mapped_rule_count
        exercises = $exerciseCount
        hints = $hintCount
        problems = $problemCount
        solutions = $solutionCount
        labels = $labels.Count
        canonical_path = $row.canonical_path
    }
}

if ($activeIncludes.Count -ne 42) {
    $issues += "book.tex must have exactly 42 active chapter includes; found $($activeIncludes.Count)."
}

$duplicateLabels = @()
$labelGroups = @($labelRecords | Group-Object -Property label -CaseSensitive)
foreach ($group in $labelGroups) {
    if ($group.Count -gt 1) {
        $duplicateLabels += $group.Name
        $owners = @($group.Group | ForEach-Object { $_.owner })
        $issues += "Duplicate label '$($group.Name)' appears in: $($owners -join ', ')"
    }
}

$unresolvedRefs = @()
foreach ($ref in $allRefs) {
    if ($ref -match '(?i)vii\d' -and -not ($allLabels -ccontains $ref)) {
        $unresolvedRefs += $ref
    }
}
$unresolvedRefs = @($unresolvedRefs | Sort-Object -Unique)
foreach ($ref in $unresolvedRefs) {
    $issues += "Unresolved Volume VII local reference target: $ref"
}

$totalExercises = [int](($chapterSummaries | Measure-Object -Property exercises -Sum).Sum)
$totalHints = [int](($chapterSummaries | Measure-Object -Property hints -Sum).Sum)
$totalProblems = [int](($chapterSummaries | Measure-Object -Property problems -Sum).Sum)
$totalSolutions = [int](($chapterSummaries | Measure-Object -Property solutions -Sum).Sum)
$totalLabels = [int](($chapterSummaries | Measure-Object -Property labels -Sum).Sum)

$ok = ($issues.Count -eq 0)

$md = @()
$md += "# Volume VII Corpus Audit"
$md += ""
$md += "**Volume:** VII — Differential, Riemannian and Hyperbolic Geometry"
$md += ""
if ($ok) {
    $md += "**Result:** PASS"
} else {
    $md += "**Result:** FAIL"
}
$md += ""
$md += "## Scope"
$md += ""
$md += "- Canonical chapter rows: $($viiRows.Count) / 42"
$md += "- Active book includes: $($activeIncludes.Count) / 42"
$md += "- Exercises: $totalExercises"
$md += "- Hints: $totalHints"
$md += "- Solved problems: $totalProblems"
$md += "- Solutions: $totalSolutions"
$md += "- Labels: $totalLabels"
$md += "- Duplicate labels: $($duplicateLabels.Count)"
$md += "- Unresolved Volume VII local references: $($unresolvedRefs.Count)"
$md += ""
$md += "## Chapter matrix"
$md += ""
$md += "| Code | Status | Next action | Exercises | Hints | Solved problems | Solutions | Labels | Canonical path |"
$md += "|---|---|---|---:|---:|---:|---:|---:|---|"
foreach ($c in $chapterSummaries) {
    $md += "| $($c.code) | $($c.status) | $($c.next_action) | $($c.exercises) | $($c.hints) | $($c.problems) | $($c.solutions) | $($c.labels) | ``$($c.canonical_path)`` |"
}
$md += ""
$md += "## Findings"
$md += ""
if ($issues.Count -eq 0) {
    $md += "- No blocking corpus-audit findings."
} else {
    foreach ($issue in $issues) {
        $md += "- BLOCKER: $issue"
    }
}
foreach ($warning in $warnings) {
    $md += "- WARNING: $warning"
}
$md += ""
$md += "## Freeze rule"
$md += ""
$md += "Volume VII may be marked frozen only after this audit passes with all 42 rows set to ``FROZEN`` / ``COMPLETE`` and a clean ``latexmk`` build has no undefined or multiply defined references."

Write-Utf8NoBom -Path $reportMd -Text (($md -join "`r`n") + "`r`n")

$jsonObject = [pscustomobject]@{
    volume = "VII"
    result = $(if ($ok) { "PASS" } else { "FAIL" })
    chapter_rows = $viiRows.Count
    active_includes = $activeIncludes.Count
    exercises = $totalExercises
    hints = $totalHints
    solved_problems = $totalProblems
    solutions = $totalSolutions
    labels = $totalLabels
    duplicate_labels = $duplicateLabels
    unresolved_local_references = $unresolvedRefs
    issues = $issues
    chapters = $chapterSummaries
}
$jsonText = $jsonObject | ConvertTo-Json -Depth 8
Write-Utf8NoBom -Path $reportJson -Text ($jsonText + "`r`n")

if (-not $ok) {
    Write-Host ""
    Write-Host "VOLUME VII CORPUS AUDIT FAILED" -ForegroundColor Red
    foreach ($issue in $issues) {
        Write-Host ("  - " + $issue) -ForegroundColor Red
    }
    throw "Volume VII corpus audit failed with $($issues.Count) blocking finding(s)."
}

Write-Host ""
Write-Host "VOLUME VII CORPUS AUDIT PASSED" -ForegroundColor Green
Write-Host "Chapters: 42"
Write-Host "Exercises / hints / solved problems / solutions: $totalExercises / $totalHints / $totalProblems / $totalSolutions"
Write-Host "Report: $reportMd"
