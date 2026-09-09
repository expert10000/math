param(
    [Parameter(Mandatory=$true)]
    [string]$Repo
)

$ErrorActionPreference = "Stop"
$Repo = (Resolve-Path $Repo).Path
$Vol = Join-Path $Repo "books\vol08_algebraic_topology"
$Book = Join-Path $Vol "book.tex"
$Status = Join-Path $Repo "editorial\CHAPTER_STATUS.tsv"

function Read-Text([string]$Path) {
    return [System.IO.File]::ReadAllText($Path)
}

$bookText = Read-Text $Book

$includeMatches = @([regex]::Matches(
    $bookText,
    '(?m)^[ \t]*\\include\{(chapters/ch(\d\d)_[^}]+/chapter)\}'
))
$pedMatches = @([regex]::Matches(
    $bookText,
    '(?m)^[ \t]*\\input\{(chapters/ch(\d\d)_[^}]+/pedagogy_expansion)\}'
))

$errors = @()

if ($includeMatches.Count -ne 35) {
    $errors += "Expected 35 canonical chapter includes, found $($includeMatches.Count)."
}
if ($pedMatches.Count -ne 35) {
    $errors += "Expected 35 active pedagogy-expansion inputs, found $($pedMatches.Count)."
}

$active = @()
foreach ($m in $includeMatches) {
    $active += [pscustomobject]@{
        Kind = "canonical"
        Code = "VIII/" + $m.Groups[2].Value
        Path = Join-Path $Vol ($m.Groups[1].Value.Replace("/", "\") + ".tex")
    }
}
foreach ($m in $pedMatches) {
    $active += [pscustomobject]@{
        Kind = "pedagogy"
        Code = "VIII/" + $m.Groups[2].Value
        Path = Join-Path $Vol ($m.Groups[1].Value.Replace("/", "\") + ".tex")
    }
}

$labels = @()
$refs = @()
$rows = @()

foreach ($s in $active) {
    if (-not (Test-Path -LiteralPath $s.Path)) {
        $errors += "Missing active source: $($s.Path)"
        continue
    }

    $t = Read-Text $s.Path

    foreach ($m in [regex]::Matches($t, '\\label\{([^}]+)\}')) {
        $labels += $m.Groups[1].Value
    }
    foreach ($m in [regex]::Matches($t, '\\(?:ref|eqref|autoref)\{([^}]+)\}')) {
        $refs += $m.Groups[1].Value
    }

    $exercise = ([regex]::Matches($t, '\\begin\{exercise\}')).Count
    $hint = ([regex]::Matches($t, '\\begin\{hint\}')).Count
    $problem = ([regex]::Matches($t, '\\begin\{problem\}')).Count
    $solution = ([regex]::Matches($t, '\\begin\{solution\}')).Count

    if ($hint -ne $exercise) {
        $errors += "$($s.Code) $($s.Kind): exercises=$exercise hints=$hint"
    }

    if ($s.Kind -eq "canonical") {
        if ($solution -ne ($exercise + $problem)) {
            $errors += "$($s.Code) canonical: solutions=$solution expected=$($exercise + $problem) (exercises+problems)"
        }
    } else {
        if ($problem -ne 0) {
            $errors += "$($s.Code) pedagogy: unexpected solved-problem environments=$problem"
        }
        if ($solution -ne $exercise) {
            $errors += "$($s.Code) pedagogy: solutions=$solution expected=$exercise"
        }
    }

    if ($t -match '(?i)\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b') {
        $errors += "$($s.Code) $($s.Kind): placeholder marker detected"
    }

    $rows += [pscustomobject]@{
        Code = $s.Code
        Kind = $s.Kind
        Exercises = $exercise
        Hints = $hint
        Problems = $problem
        Solutions = $solution
    }
}

$dupLabels = @($labels | Group-Object | Where-Object Count -gt 1 | Sort-Object Name)
if ($dupLabels.Count -gt 0) {
    $errors += "Duplicate labels across active canonical+pedagogy sources: $($dupLabels.Count)"
    foreach ($d in $dupLabels | Select-Object -First 20) {
        $errors += "  duplicate label: $($d.Name) x$($d.Count)"
    }
}

$labelSet = @{}
foreach ($l in $labels) { $labelSet[$l] = $true }
$missingRefs = @($refs | Sort-Object -Unique | Where-Object {
    ($_ -match '(?i)viii\d\d') -and (-not $labelSet.ContainsKey($_))
})
if ($missingRefs.Count -gt 0) {
    $errors += "Missing Volume-VIII refs across active canonical+pedagogy sources: $($missingRefs.Count)"
    foreach ($r in $missingRefs | Select-Object -First 20) {
        $errors += "  missing ref: $r"
    }
}

$statusRows = @(Import-Csv -LiteralPath $Status -Delimiter "`t" |
    Where-Object { $_.volume -eq "VIII" })
if ($statusRows.Count -ne 35) {
    $errors += "Expected 35 Volume VIII status rows, found $($statusRows.Count)."
}
foreach ($r in $statusRows) {
    if ($r.status -ne "FROZEN" -or $r.next_action -ne "COMPLETE") {
        $errors += "Status mismatch $($r.chapter_code): status=$($r.status) next_action=$($r.next_action)"
    }
}

Write-Host "Volume VIII active-source professional audit:" -ForegroundColor Cyan
Write-Host "  canonical=$($includeMatches.Count) pedagogy=$($pedMatches.Count)"
Write-Host "  active_sources=$($active.Count) labels=$($labels.Count)"
Write-Host "  exercises=$((($rows | Measure-Object Exercises -Sum).Sum))"
Write-Host "  hints=$((($rows | Measure-Object Hints -Sum).Sum))"
Write-Host "  problems=$((($rows | Measure-Object Problems -Sum).Sum))"
Write-Host "  solutions=$((($rows | Measure-Object Solutions -Sum).Sum))"

if ($errors.Count -gt 0) {
    Write-Host "VOLUME VIII ACTIVE-SOURCE AUDIT FAILED" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host "BLOCK: $_" }
    exit 2
}

Write-Host "VOLUME VIII ACTIVE-SOURCE AUDIT PASSED" -ForegroundColor Green
