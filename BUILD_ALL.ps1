param(
    [switch]$CanonicalOnly,
    [switch]$CleanFirst,
    [switch]$FailFast,
    [switch]$NoPdfCollection
)

$ErrorActionPreference = "Stop"

# BUILD_ALL.ps1
# Compile all canonical volume books under books/vol*/book.tex.
# By default, also compile any root-level edition wrappers matching:
#   part*_student.tex
#   part*_hints.tex
#   part*_complete.tex
#
# Run this script from anywhere. The repository root is inferred from
# the script location, so it is safest to keep this file in the repo root.

$Repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$Books = Join-Path $Repo "books"
$CollectedPdfDir = Join-Path $Repo "build\pdf"

if (-not (Test-Path (Join-Path $Repo ".git"))) {
    throw "BUILD_ALL.ps1 must be stored in the repository root."
}

if (-not (Test-Path $Books)) {
    throw "Missing books directory: $Books"
}

if (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) {
    throw "latexmk is not available on PATH. Install/configure MiKTeX or TeX Live first."
}

if (-not $NoPdfCollection) {
    New-Item -ItemType Directory -Force -Path $CollectedPdfDir | Out-Null
}

$volumeDirs = Get-ChildItem -Path $Books -Directory |
    Where-Object { $_.Name -match '^vol\d+_' } |
    Sort-Object Name

if (-not $volumeDirs) {
    throw "No canonical volume directories matching books/vol*_ were found."
}

$targets = New-Object System.Collections.Generic.List[object]

foreach ($vol in $volumeDirs) {
    $book = Join-Path $vol.FullName "book.tex"
    if (Test-Path $book) {
        $targets.Add([pscustomobject]@{
            Volume = $vol.Name
            File   = "book.tex"
            Kind   = "canonical"
            Dir    = $vol.FullName
        })
    }

    if (-not $CanonicalOnly) {
        $editionPatterns = @(
            "part*_student.tex",
            "part*_hints.tex",
            "part*_complete.tex"
        )

        foreach ($pattern in $editionPatterns) {
            Get-ChildItem -Path $vol.FullName -File -Filter $pattern |
                Sort-Object Name |
                ForEach-Object {
                    $targets.Add([pscustomobject]@{
                        Volume = $vol.Name
                        File   = $_.Name
                        Kind   = "edition"
                        Dir    = $vol.FullName
                    })
                }
        }
    }
}

if ($targets.Count -eq 0) {
    throw "No LaTeX build targets were found."
}

Write-Host ""
Write-Host "MATH canonical build" -ForegroundColor Cyan
Write-Host "Repository: $Repo"
Write-Host "Targets:    $($targets.Count)"
if ($CanonicalOnly) {
    Write-Host "Mode:       canonical volume books only"
} else {
    Write-Host "Mode:       canonical books + discovered student/hints/complete editions"
}
Write-Host ""

$success = New-Object System.Collections.Generic.List[object]
$failed  = New-Object System.Collections.Generic.List[object]

foreach ($target in $targets) {
    $label = "$($target.Volume) / $($target.File)"
    Write-Host "============================================================" -ForegroundColor DarkGray
    Write-Host "BUILD: $label" -ForegroundColor Cyan

    Push-Location $target.Dir
    try {
        if ($CleanFirst) {
            Write-Host "Cleaning previous auxiliary files..."
            & latexmk -C $target.File
            if ($LASTEXITCODE -ne 0) {
                throw "latexmk clean failed with exit code $LASTEXITCODE"
            }
        }

        & latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error $target.File
        if ($LASTEXITCODE -ne 0) {
            throw "latexmk failed with exit code $LASTEXITCODE"
        }

        $pdfName = [System.IO.Path]::ChangeExtension($target.File, ".pdf")
        $pdfPath = Join-Path $target.Dir $pdfName

        if (-not (Test-Path $pdfPath)) {
            throw "latexmk returned success but PDF was not found: $pdfPath"
        }

        $pdf = Get-Item $pdfPath

        if (-not $NoPdfCollection) {
            $safeTarget = [System.IO.Path]::GetFileNameWithoutExtension($target.File)
            $destName = "$($target.Volume)_$safeTarget.pdf"
            Copy-Item -Force $pdf.FullName (Join-Path $CollectedPdfDir $destName)
        }

        $success.Add([pscustomobject]@{
            Target = $label
            Pdf    = $pdf.FullName
            SizeMB = [math]::Round($pdf.Length / 1MB, 2)
        })

        Write-Host "OK: $pdfName ($([math]::Round($pdf.Length / 1MB, 2)) MB)" -ForegroundColor Green
    }
    catch {
        $failed.Add([pscustomobject]@{
            Target = $label
            Error  = $_.Exception.Message
        })

        Write-Host "FAILED: $label" -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red

        if ($FailFast) {
            throw
        }
    }
    finally {
        Pop-Location
    }

    Write-Host ""
}

Write-Host "============================================================" -ForegroundColor DarkGray
Write-Host "BUILD SUMMARY" -ForegroundColor Cyan
Write-Host "Succeeded: $($success.Count)"
Write-Host "Failed:    $($failed.Count)"

if ($success.Count -gt 0) {
    Write-Host ""
    Write-Host "Successful targets:" -ForegroundColor Green
    $success | Format-Table -AutoSize Target, SizeMB
}

if ($failed.Count -gt 0) {
    Write-Host ""
    Write-Host "Failed targets:" -ForegroundColor Red
    $failed | Format-Table -AutoSize Target, Error
}

if (-not $NoPdfCollection) {
    Write-Host ""
    Write-Host "Collected PDFs:" -ForegroundColor Cyan
    Write-Host "  $CollectedPdfDir"
}

if ($failed.Count -gt 0) {
    exit 1
}

exit 0
