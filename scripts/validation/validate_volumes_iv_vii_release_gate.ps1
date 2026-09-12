param(
    [Parameter(Mandatory=$true)]
    [string]$Repo
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Write-Utf8NoBom([string]$Path, [string]$Text) {
    $enc = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $enc)
}

function Invoke-CleanBuild([string]$BookDir) {
    $latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
    $pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue

    Push-Location $BookDir
    try {
        if ($latexmk) {
            & $latexmk.Source -C book.tex | Out-Host
            if ($LASTEXITCODE -ne 0) { throw "latexmk clean failed: $BookDir" }

            & $latexmk.Source -pdf -interaction=nonstopmode -halt-on-error book.tex | Out-Host
            if ($LASTEXITCODE -ne 0) { throw "latexmk build failed: $BookDir" }

            & $latexmk.Source -pdf -interaction=nonstopmode -halt-on-error book.tex | Out-Host
            if ($LASTEXITCODE -ne 0) { throw "second latexmk build failed: $BookDir" }
        }
        elseif ($pdflatex) {
            @("book.aux","book.log","book.out","book.toc","book.fls","book.fdb_latexmk","book.pdf") | ForEach-Object {
                if (Test-Path $_) { Remove-Item $_ -Force }
            }

            & $pdflatex.Source -interaction=nonstopmode -halt-on-error book.tex | Out-Host
            if ($LASTEXITCODE -ne 0) { throw "pdflatex build failed: $BookDir" }

            & $pdflatex.Source -interaction=nonstopmode -halt-on-error book.tex | Out-Host
            if ($LASTEXITCODE -ne 0) { throw "second pdflatex build failed: $BookDir" }
        }
        else {
            throw "Neither latexmk nor pdflatex is available on PATH."
        }
    }
    finally {
        Pop-Location
    }
}

function Get-Warnings([string]$BookDir) {
    $log = Join-Path $BookDir "book.log"
    if (-not (Test-Path $log)) { throw "Missing build log: $log" }

    [PSCustomObject]@{
        Overfull = @(Select-String -Path $log -Pattern 'Overfull \\[hv]box').Count
        Underfull = @(Select-String -Path $log -Pattern 'Underfull \\[hv]box').Count
        Undefined = @(Select-String -Path $log -Pattern 'LaTeX Warning: (Reference|Citation) .+ undefined').Count
    }
}

function Get-PdfInfo([string]$BookDir) {
    $log = Join-Path $BookDir "book.log"
    $text = [System.IO.File]::ReadAllText($log)
    $matches = [regex]::Matches($text, 'Output written on book\.pdf \((\d+) pages?,\s*(\d+) bytes\)')
    if ($matches.Count -eq 0) {
        return [PSCustomObject]@{ Pages = 0; Bytes = 0 }
    }
    $m = $matches[$matches.Count - 1]
    return [PSCustomObject]@{
        Pages = [int]$m.Groups[1].Value
        Bytes = [int64]$m.Groups[2].Value
    }
}

function Remove-TexComments([string]$Text) {
    $lines = $Text -split "\r?\n"
    $clean = New-Object System.Collections.Generic.List[string]

    foreach ($line in $lines) {
        # Strip only unescaped TeX comments.  This is sufficient for the
        # repository's source style and preserves escaped percent signs.
        $clean.Add(([regex]::Replace($line, '(?<!\\)%.*$', '')))
    }

    return ($clean -join "`n")
}

function Resolve-TexTarget(
    [string]$BookDir,
    [string]$IncludingFile,
    [string]$RawPath
) {
    $rawNative = $RawPath -replace '/', '\'
    $candidates = New-Object System.Collections.Generic.List[string]

    # TeX is run from BookDir, so try cwd-relative first.
    $candidates.Add((Join-Path $BookDir $rawNative))

    # Also support file-relative includes used by some local fragments.
    if ($IncludingFile) {
        $parent = Split-Path -Parent $IncludingFile
        $candidates.Add((Join-Path $parent $rawNative))
    }

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate -PathType Leaf) {
            return (Resolve-Path $candidate).Path
        }

        if (-not [System.IO.Path]::HasExtension($candidate)) {
            $withTex = $candidate + ".tex"
            if (Test-Path $withTex -PathType Leaf) {
                return (Resolve-Path $withTex).Path
            }
        }
    }

    return $null
}

function Get-ActiveTexGraph([string]$BookDir) {
    $bookPath = (Resolve-Path (Join-Path $BookDir "book.tex")).Path

    $visited = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)
    $active = New-Object System.Collections.Generic.List[string]
    $missing = New-Object System.Collections.Generic.List[string]
    $queue = New-Object System.Collections.Generic.Queue[string]
    $queue.Enqueue($bookPath)

    while ($queue.Count -gt 0) {
        $file = $queue.Dequeue()
        if (-not $visited.Add($file)) { continue }

        $active.Add($file)

        $rawText = [System.IO.File]::ReadAllText($file)
        $text = Remove-TexComments $rawText
        $matches = [regex]::Matches($text, '\\(?:include|input)\{([^}]+)\}')

        foreach ($m in $matches) {
            $raw = $m.Groups[1].Value.Trim()
            $target = Resolve-TexTarget $BookDir $file $raw

            if ($null -eq $target) {
                $missing.Add(("{0} -> {1}" -f $file, $raw))
            }
            elseif ([System.IO.Path]::GetExtension($target).ToLowerInvariant() -eq ".tex") {
                if (-not $visited.Contains($target)) {
                    $queue.Enqueue($target)
                }
            }
        }
    }

    return [PSCustomObject]@{
        Files = @($active)
        Missing = @($missing)
    }
}

function Get-LabelDuplicates([string[]]$TexFiles) {
    # TeX labels are case-sensitive.
    $counts = New-Object 'System.Collections.Generic.Dictionary[string,int]' ([System.StringComparer]::Ordinal)

    foreach ($file in $TexFiles) {
        $text = Remove-TexComments ([System.IO.File]::ReadAllText($file))
        $matches = [regex]::Matches($text, '\\label\{([^}]+)\}')

        foreach ($m in $matches) {
            $label = $m.Groups[1].Value
            if ($counts.ContainsKey($label)) {
                $counts[$label] = $counts[$label] + 1
            }
            else {
                $counts.Add($label, 1)
            }
        }
    }

    $dups = New-Object System.Collections.Generic.List[string]
    foreach ($entry in $counts.GetEnumerator()) {
        if ($entry.Value -gt 1) {
            $dups.Add($entry.Key)
        }
    }

    return @($dups)
}

function Get-EnvironmentCounts([string[]]$TexFiles) {
    $all = New-Object System.Text.StringBuilder

    foreach ($file in $TexFiles) {
        $text = Remove-TexComments ([System.IO.File]::ReadAllText($file))
        [void]$all.AppendLine($text)
    }

    $text = $all.ToString()

    $problemBegin = ([regex]::Matches($text, '\\begin\{problem\}')).Count
    $problemEnd = ([regex]::Matches($text, '\\end\{problem\}')).Count
    $exerciseBegin = ([regex]::Matches($text, '\\begin\{exercise\}')).Count
    $exerciseEnd = ([regex]::Matches($text, '\\end\{exercise\}')).Count
    $hintBegin = ([regex]::Matches($text, '\\begin\{hint\}')).Count
    $hintEnd = ([regex]::Matches($text, '\\end\{hint\}')).Count
    $solutionBegin = ([regex]::Matches($text, '\\begin\{solution\}')).Count
    $solutionEnd = ([regex]::Matches($text, '\\end\{solution\}')).Count

    return [PSCustomObject]@{
        Problems = $problemBegin
        Exercises = $exerciseBegin
        Hints = $hintBegin
        Solutions = $solutionBegin
        ProblemEnds = $problemEnd
        ExerciseEnds = $exerciseEnd
        HintEnds = $hintEnd
        SolutionEnds = $solutionEnd
        Balanced = (
            $problemBegin -eq $problemEnd -and
            $exerciseBegin -eq $exerciseEnd -and
            $hintBegin -eq $hintEnd -and
            $solutionBegin -eq $solutionEnd
        )
    }
}

function Test-Assets(
    [string]$RepoPath,
    [string]$BookDir,
    [string[]]$TexFiles
) {
    $missing = New-Object System.Collections.Generic.List[string]
    $exts = @("", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg")

    foreach ($file in $TexFiles) {
        $text = Remove-TexComments ([System.IO.File]::ReadAllText($file))
        $matches = [regex]::Matches($text, '\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}')

        foreach ($m in $matches) {
            $asset = $m.Groups[1].Value
            $found = $false

            foreach ($ext in $exts) {
                $name = $asset

                if ((-not [System.IO.Path]::HasExtension($asset)) -and ($ext -ne "")) {
                    $name = $asset + $ext
                }
                elseif ([System.IO.Path]::HasExtension($asset) -and ($ext -ne "")) {
                    continue
                }

                $candidates = @(
                    (Join-Path $BookDir ($name -replace '/', '\')),
                    (Join-Path (Split-Path -Parent $file) ($name -replace '/', '\')),
                    (Join-Path (Join-Path $RepoPath "figures") ($name -replace '/', '\'))
                )

                foreach ($candidate in $candidates) {
                    if (Test-Path $candidate -PathType Leaf) {
                        $found = $true
                        break
                    }
                }

                if ($found) { break }
            }

            if (-not $found) {
                $missing.Add(("{0} -> {1}" -f $file, $asset))
            }
        }
    }

    return @($missing | Sort-Object -Unique)
}

function Get-ObsoleteMarkerCount([string[]]$TexFiles) {
    # Active expansion/pedagogy markers were explicitly retained by the marker
    # classification audit because validation consumes them.  Only the obsolete
    # hint-reconciliation family is prohibited.
    $patterns = @(
        'VOL04-HINT-RECONCILIATION'
    )

    $count = 0
    foreach ($file in $TexFiles) {
        $text = [System.IO.File]::ReadAllText($file)
        foreach ($pattern in $patterns) {
            $count += ([regex]::Matches($text, [regex]::Escape($pattern))).Count
        }
    }

    return $count
}

$Repo = (Resolve-Path $Repo).Path

$volumes = @(
    [PSCustomObject]@{ Volume="IV"; Path="books\vol04_complex_analysis"; ExpectedChapters=31; MaxOverfull=0; MaxUnderfull=0 },
    [PSCustomObject]@{ Volume="V"; Path="books\vol05_commutative_algebra"; ExpectedChapters=28; MaxOverfull=0; MaxUnderfull=0 },
    [PSCustomObject]@{ Volume="VI"; Path="books\vol06_algebraic_geometry"; ExpectedChapters=49; MaxOverfull=6; MaxUnderfull=20 },
    [PSCustomObject]@{ Volume="VII"; Path="books\vol07_differential_geometry"; ExpectedChapters=42; MaxOverfull=0; MaxUnderfull=7 }
)

$results = New-Object System.Collections.Generic.List[object]
$overallPass = $true

foreach ($v in $volumes) {
    $bookDir = Join-Path $Repo $v.Path
    if (-not (Test-Path $bookDir)) { throw "Missing volume directory: $bookDir" }

    Write-Host ""
    Write-Host "=== Volume $($v.Volume) clean build ===" -ForegroundColor Cyan
    Invoke-CleanBuild $bookDir

    $warnings = Get-Warnings $bookDir
    $pdfInfo = Get-PdfInfo $bookDir
    $bookText = Remove-TexComments ([System.IO.File]::ReadAllText((Join-Path $bookDir "book.tex")))
    $chapterCount = ([regex]::Matches($bookText, '\\include\{chapters/')).Count

    $graph = Get-ActiveTexGraph $bookDir

    # For manuscript integrity checks, scan only active volume-local TeX files.
    # Shared preamble/macro files are validated as graph inputs but are not
    # counted as volume labels/exercises.
    $bookRoot = (Resolve-Path $bookDir).Path.TrimEnd('\') + '\'
    $localTexFiles = @(
        $graph.Files | Where-Object {
            $_.StartsWith($bookRoot, [System.StringComparison]::OrdinalIgnoreCase)
        }
    )

    $missingInputs = @($graph.Missing)
    $duplicates = @(Get-LabelDuplicates $localTexFiles)
    $env = Get-EnvironmentCounts $localTexFiles
    $missingAssets = @(Test-Assets $Repo $bookDir $localTexFiles)
    $obsoleteMarkers = Get-ObsoleteMarkerCount $localTexFiles

    $tocOk = Test-Path (Join-Path $bookDir "book.toc")
    $pdfOk = Test-Path (Join-Path $bookDir "book.pdf")

    # All active pedagogical environments must be syntactically balanced.
    $environmentBalance = $env.Balanced

    # Volumes IV, V and VII use the main-book convention in which exercises
    # carry hints and the combined problem/exercise layer is fully solved.
    # Volume VI intentionally separates part of its full-solution apparatus
    # into book_full_solutions.tex, so applying that ratio to book.tex would
    # reject a valid publication design.  VI is gated by environment balance,
    # active-graph integrity and its successful full PDF build instead.
    $solutionCoverage = $true
    $hintCoverage = $true
    if ($v.Volume -ne "VI") {
        $solutionCoverage = $env.Solutions -ge ($env.Problems + $env.Exercises)
        $hintCoverage = $env.Hints -ge $env.Exercises
    }

    $pass = (
        $chapterCount -eq $v.ExpectedChapters -and
        $missingInputs.Count -eq 0 -and
        $duplicates.Count -eq 0 -and
        $missingAssets.Count -eq 0 -and
        $obsoleteMarkers -eq 0 -and
        $warnings.Undefined -eq 0 -and
        $warnings.Overfull -le $v.MaxOverfull -and
        $warnings.Underfull -le $v.MaxUnderfull -and
        $environmentBalance -and
        $solutionCoverage -and
        $hintCoverage -and
        $tocOk -and
        $pdfOk -and
        $pdfInfo.Pages -gt 0
    )

    if (-not $pass) { $overallPass = $false }

    $results.Add([PSCustomObject]@{
        Volume = $v.Volume
        Status = $(if ($pass) { "PASS" } else { "FAIL" })
        Chapters = $chapterCount
        ExpectedChapters = $v.ExpectedChapters
        Overfull = $warnings.Overfull
        Underfull = $warnings.Underfull
        Undefined = $warnings.Undefined
        DuplicateLabels = $duplicates.Count
        MissingInputs = $missingInputs.Count
        MissingAssets = $missingAssets.Count
        ObsoleteMarkers = $obsoleteMarkers
        Problems = $env.Problems
        Exercises = $env.Exercises
        Hints = $env.Hints
        Solutions = $env.Solutions
        Pages = $pdfInfo.Pages
        PdfBytes = $pdfInfo.Bytes
        ActiveTexFiles = $localTexFiles.Count
        EnvironmentBalanced = $env.Balanced
    })

    Write-Host ("Volume {0}: {1} | chapters={2}/{3} | overfull={4} | underfull={5} | undefined={6} | dupLabels={7} | missingInputs={8} | missingAssets={9} | envBalanced={10}" -f `
        $v.Volume, $(if ($pass) { "PASS" } else { "FAIL" }), $chapterCount, $v.ExpectedChapters, `
        $warnings.Overfull, $warnings.Underfull, $warnings.Undefined, $duplicates.Count, $missingInputs.Count, $missingAssets.Count, $env.Balanced)
}

$reviewDir = Join-Path $Repo "docs\review"
if (-not (Test-Path $reviewDir)) { New-Item -ItemType Directory -Path $reviewDir | Out-Null }

$tsvPath = Join-Path $reviewDir "VOLUMES_IV_VII_FINAL_REGRESSION.tsv"
$mdPath = Join-Path $reviewDir "VOLUMES_IV_VII_FINAL_REGRESSION.md"

$header = "volume`tstatus`tchapters`texpected_chapters`toverfull`tunderfull`tundefined`tduplicate_labels`tmissing_inputs`tmissing_assets`tobsolete_markers`tproblems`texercises`thints`tsolutions`tpages`tpdf_bytes`tactive_tex_files`tenvironment_balanced"
$rows = New-Object System.Collections.Generic.List[string]
$rows.Add($header)
foreach ($r in $results) {
    $rows.Add((
        "{0}`t{1}`t{2}`t{3}`t{4}`t{5}`t{6}`t{7}`t{8}`t{9}`t{10}`t{11}`t{12}`t{13}`t{14}`t{15}`t{16}`t{17}`t{18}" -f `
        $r.Volume,$r.Status,$r.Chapters,$r.ExpectedChapters,$r.Overfull,$r.Underfull,$r.Undefined,`
        $r.DuplicateLabels,$r.MissingInputs,$r.MissingAssets,$r.ObsoleteMarkers,$r.Problems,$r.Exercises,`
        $r.Hints,$r.Solutions,$r.Pages,$r.PdfBytes,$r.ActiveTexFiles,$r.EnvironmentBalanced
    ))
}
Write-Utf8NoBom $tsvPath (($rows -join "`n") + "`n")

$head = ""
Push-Location $Repo
try { $head = (& git rev-parse HEAD).Trim() } finally { Pop-Location }

$md = New-Object System.Collections.Generic.List[string]
$md.Add("# Volumes IV-VII final regression gate")
$md.Add("")
$md.Add("Source HEAD before gate commit: ``$head``")
$md.Add("")
$md.Add("Overall status: **$(if ($overallPass) { 'PASS' } else { 'FAIL' })**")
$md.Add("")
$md.Add("| Volume | Status | Chapters | Overfull | Underfull | Undefined | Duplicate labels | Missing inputs | Missing assets | Pages |")
$md.Add("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
foreach ($r in $results) {
    $md.Add("| $($r.Volume) | $($r.Status) | $($r.Chapters)/$($r.ExpectedChapters) | $($r.Overfull) | $($r.Underfull) | $($r.Undefined) | $($r.DuplicateLabels) | $($r.MissingInputs) | $($r.MissingAssets) | $($r.Pages) |")
}
$md.Add("")
$md.Add("Gate checks:")
$md.Add("")
$md.Add("- clean two-pass PDF build for each volume")
$md.Add("- expected chapter include count")
$md.Add("- all TeX inputs resolve")
$md.Add("- zero duplicate labels")
$md.Add("- zero undefined references/citations")
$md.Add("- asset references resolve")
$md.Add("- balanced problem/exercise/hint/solution environments; main-book hint/solution coverage where that volume uses the convention")
$md.Add("- obsolete reconstruction-marker gate")
$md.Add("- TOC and PDF artifacts produced")
$md.Add("- layout-warning thresholds: IV 0/0, V 0/0, VI 6/20, VII 0/7 (overfull/underfull)")
$md.Add("")
Write-Utf8NoBom $mdPath (($md -join "`n") + "`n")

if (-not $overallPass) {
    throw "Volumes IV-VII final regression gate FAILED. See $mdPath"
}

Write-Host ""
Write-Host "FINAL REGRESSION GATE: PASS" -ForegroundColor Green
