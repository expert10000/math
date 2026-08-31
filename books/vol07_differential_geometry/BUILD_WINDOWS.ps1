param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "",

    [switch]$Clean,

    [switch]$SkipAudit
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Repo)) {
    $Repo = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
} else {
    $Repo = (Resolve-Path $Repo).Path
}

$vol = Join-Path $Repo "books/vol07_differential_geometry"
$book = Join-Path $vol "book.tex"
$audit = Join-Path $vol "AUDIT_VOLUME07.ps1"

if (-not (Test-Path -LiteralPath $book)) {
    throw "Missing Volume VII wrapper: $book"
}
if (-not (Test-Path -LiteralPath $audit)) {
    throw "Missing Volume VII audit script: $audit"
}

if (-not $SkipAudit) {
    & powershell -NoProfile -ExecutionPolicy Bypass -File $audit -Repo $Repo
    if ($LASTEXITCODE -ne 0) {
        throw "Volume VII pre-build corpus audit failed."
    }
}

$latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
if (-not $latexmk) {
    throw "latexmk was not found on PATH. Install/enable MiKTeX latexmk, then rerun."
}

Push-Location $vol
try {
    if ($Clean) {
        & latexmk -C book.tex
        if ($LASTEXITCODE -ne 0) {
            throw "latexmk clean failed with exit code $LASTEXITCODE"
        }
    }

    & latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
    if ($LASTEXITCODE -ne 0) {
        throw "Volume VII latexmk build failed with exit code $LASTEXITCODE"
    }

    $logPath = Join-Path $vol "book.log"
    if (-not (Test-Path -LiteralPath $logPath)) {
        throw "Volume VII build completed without expected book.log."
    }

    $badPatterns = @(
        "LaTeX Warning: There were undefined references",
        "LaTeX Warning: Label(s) may have changed",
        "multiply defined",
        "There were undefined citations"
    )

    $logText = [System.IO.File]::ReadAllText($logPath)
    $bad = @()
    foreach ($pattern in $badPatterns) {
        if ($logText.IndexOf($pattern, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
            $bad += $pattern
        }
    }

    if ($bad.Count -gt 0) {
        throw ("Volume VII post-build reference regression failed: " + ($bad -join "; "))
    }

    $pdfPath = Join-Path $vol "book.pdf"
    if (-not (Test-Path -LiteralPath $pdfPath)) {
        throw "Volume VII PDF was not produced: $pdfPath"
    }

    Write-Host ""
    Write-Host "VOLUME VII BUILD PASSED" -ForegroundColor Green
    Write-Host ("PDF: " + $pdfPath)
}
finally {
    Pop-Location
}
