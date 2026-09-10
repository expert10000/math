param(
    [Parameter(Mandatory=$true)]
    [string]$Repo
)

$ErrorActionPreference = "Stop"
$Repo = (Resolve-Path $Repo).Path
$Vol = Join-Path $Repo "books\vol01_linear_algebra"
$Book = Join-Path $Vol "book.tex"
$Status = Join-Path $Repo "editorial\CHAPTER_STATUS.tsv"

function Read-Text([string]$Path) {
    return [System.IO.File]::ReadAllText($Path)
}

if (-not (Test-Path -LiteralPath $Book)) {
    throw "Missing Volume I book.tex: $Book"
}
if (-not (Test-Path -LiteralPath $Status)) {
    throw "Missing chapter-status ledger: $Status"
}

$bookText = Read-Text $Book
$includeMatches = @([regex]::Matches(
    $bookText,
    '(?m)^[ \t]*\\include\{(chapters/ch(\d\d)_[^}]+/chapter)\}'
))

$errors = @()

if ($includeMatches.Count -ne 18) {
    $errors += "Expected 18 canonical chapter includes, found $($includeMatches.Count)."
}

$active = @()
$codes = @()
foreach ($m in $includeMatches) {
    $num = $m.Groups[2].Value
    $code = "I/" + $num
    $codes += $code
    $active += [pscustomobject]@{
        Code = $code
        Path = Join-Path $Vol ($m.Groups[1].Value.Replace("/", "\") + ".tex")
    }
}

$expectedCodes = 1..18 | ForEach-Object { "I/{0:D2}" -f $_ }
if (($codes -join "|") -ne ($expectedCodes -join "|")) {
    $errors += "Active chapter sequence is not exactly I/01 through I/18."
}

$allTex = @(Get-ChildItem -LiteralPath $Vol -Recurse -File -Filter *.tex)
$labels = @()
$refs = @()

foreach ($p in $allTex) {
    $t = Read-Text $p.FullName
    foreach ($m in [regex]::Matches($t, '\\label\{([^}]+)\}')) {
        $labels += $m.Groups[1].Value
    }
    foreach ($m in [regex]::Matches($t, '\\(?:ref|eqref|autoref)\{([^}]+)\}')) {
        $refs += $m.Groups[1].Value
    }
}

$dupLabels = @($labels | Group-Object | Where-Object Count -gt 1 | Sort-Object Name)
if ($dupLabels.Count -gt 0) {
    $errors += "Duplicate labels across Volume I TeX sources: $($dupLabels.Count)"
    foreach ($d in $dupLabels | Select-Object -First 20) {
        $errors += "  duplicate label: $($d.Name) x$($d.Count)"
    }
}

$labelSet = @{}
foreach ($l in $labels) { $labelSet[$l] = $true }

$internalRefs = @($refs | Sort-Object -Unique | Where-Object {
    $_ -match '^(?:ch|sec|thm|lem|prop|cor|def|ex|exr|prob|eq):i'
})
$missingRefs = @($internalRefs | Where-Object { -not $labelSet.ContainsKey($_) })
if ($missingRefs.Count -gt 0) {
    $errors += "Missing Volume I internal refs: $($missingRefs.Count)"
    foreach ($r in $missingRefs | Select-Object -First 20) {
        $errors += "  missing ref: $r"
    }
}

$rows = @()

foreach ($s in $active) {
    if (-not (Test-Path -LiteralPath $s.Path)) {
        $errors += "Missing active source: $($s.Path)"
        continue
    }

    $t = Read-Text $s.Path

    $theoremBegin = ([regex]::Matches($t, '\\begin\{theorem\}')).Count
    $theoremEnd   = ([regex]::Matches($t, '\\end\{theorem\}')).Count
    $proofBegin   = ([regex]::Matches($t, '\\begin\{proof\}')).Count
    $proofEnd     = ([regex]::Matches($t, '\\end\{proof\}')).Count
    $exercise     = ([regex]::Matches($t, '\\begin\{exercise\}')).Count
    $hint         = ([regex]::Matches($t, '\\begin\{hint\}')).Count
    $problem      = ([regex]::Matches($t, '\\begin\{problem\}')).Count
    $solution     = ([regex]::Matches($t, '\\begin\{solution\}')).Count

    if ($theoremBegin -ne $theoremEnd) {
        $errors += "$($s.Code): theorem begin/end mismatch $theoremBegin/$theoremEnd"
    }
    if ($proofBegin -ne $proofEnd) {
        $errors += "$($s.Code): proof begin/end mismatch $proofBegin/$proofEnd"
    }
    if ($theoremBegin -lt 1) {
        $errors += "$($s.Code): no canonical theorem environment found"
    }
    if ($proofBegin -lt $theoremBegin) {
        $errors += "$($s.Code): proofs=$proofBegin fewer than theorems=$theoremBegin"
    }
    if ($exercise -lt 8) {
        $errors += "$($s.Code): exercises=$exercise below established short-exercise floor 8"
    }
    if ($hint -ne $exercise) {
        $errors += "$($s.Code): exercises=$exercise hints=$hint"
    }
    if ($problem -lt 12) {
        $errors += "$($s.Code): solved problems=$problem below established dossier floor 12"
    }
    if ($solution -ne ($exercise + $problem)) {
        $errors += "$($s.Code): solutions=$solution expected=$($exercise + $problem) (exercises+problems)"
    }
    if ($t -match '(?i)\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b') {
        $errors += "$($s.Code): placeholder marker detected"
    }

    $theoremBlocks = @([regex]::Matches(
        $t,
        '(?s)\\begin\{theorem\}(?:\[[^\]]*\])?.*?\\end\{theorem\}'
    ))
    $withoutProof = 0
    foreach ($block in $theoremBlocks) {
        if ($block.Value -notmatch '\\begin\{proof\}') {
            $withoutProof++
        }
    }
    if ($withoutProof -gt 0) {
        $errors += "$($s.Code): theorem blocks without embedded proof=$withoutProof"
    }

    $rows += [pscustomobject]@{
        Code = $s.Code
        Theorems = $theoremBegin
        Proofs = $proofBegin
        Exercises = $exercise
        Hints = $hint
        Problems = $problem
        Solutions = $solution
    }
}

$statusRows = @(Import-Csv -LiteralPath $Status -Delimiter "`t" |
    Where-Object { $_.volume -eq "I" })

if ($statusRows.Count -ne 18) {
    $errors += "Expected 18 Volume I status rows, found $($statusRows.Count)."
}
foreach ($r in $statusRows) {
    if ($r.status -ne "FROZEN" -or $r.next_action -ne "COMPLETE") {
        $errors += "Status mismatch $($r.chapter_code): status=$($r.status) next_action=$($r.next_action)"
    }
}

Write-Host "Volume I active-source professional audit" -ForegroundColor Cyan
Write-Host "  canonical chapters: $($includeMatches.Count)"
Write-Host "  TeX sources scanned: $($allTex.Count)"
Write-Host "  unique labels: $((@($labels | Sort-Object -Unique)).Count)"
Write-Host "  internal refs: $($internalRefs.Count)"
Write-Host ""
Write-Host ("{0,-6} {1,8} {2,8} {3,10} {4,7} {5,9} {6,10}" -f `
    "Code","Theorem","Proof","Exercise","Hint","Problem","Solution")
foreach ($r in $rows) {
    Write-Host ("{0,-6} {1,8} {2,8} {3,10} {4,7} {5,9} {6,10}" -f `
        $r.Code,$r.Theorems,$r.Proofs,$r.Exercises,$r.Hints,$r.Problems,$r.Solutions)
}

Write-Host ""
Write-Host "Totals:"
Write-Host "  theorems=$((($rows | Measure-Object Theorems -Sum).Sum))"
Write-Host "  proofs=$((($rows | Measure-Object Proofs -Sum).Sum))"
Write-Host "  exercises=$((($rows | Measure-Object Exercises -Sum).Sum))"
Write-Host "  hints=$((($rows | Measure-Object Hints -Sum).Sum))"
Write-Host "  problems=$((($rows | Measure-Object Problems -Sum).Sum))"
Write-Host "  solutions=$((($rows | Measure-Object Solutions -Sum).Sum))"

if ($errors.Count -gt 0) {
    Write-Host ""
    Write-Host "VOLUME I ACTIVE-SOURCE AUDIT FAILED" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host "BLOCK: $_" }
    exit 2
}

Write-Host ""
Write-Host "VOLUME I ACTIVE-SOURCE AUDIT PASSED" -ForegroundColor Green
exit 0
