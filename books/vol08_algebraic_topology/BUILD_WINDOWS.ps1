param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "",

    [switch]$Clean
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Repo)) {
    $Repo = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
} else {
    $Repo = (Resolve-Path $Repo).Path
}

$vol = Join-Path $Repo "books/vol08_algebraic_topology"
$book = Join-Path $vol "book.tex"

if (-not (Test-Path -LiteralPath $book)) {
    throw "Missing Volume VIII wrapper: $book"
}

$bookText = [System.IO.File]::ReadAllText($book)
$matches = [regex]::Matches($bookText, '(?m)^[ \t]*\\include\{([^}]+)\}')
$includes = @($matches | ForEach-Object { $_.Groups[1].Value })

if ($includes.Count -lt 1) {
    throw "Volume VIII book.tex has no active reconstructed chapters."
}

foreach ($inc in $includes) {
    $chapter = Join-Path $vol ($inc.Replace("/", [System.IO.Path]::DirectorySeparatorChar) + ".tex")
    if (-not (Test-Path -LiteralPath $chapter)) {
        throw "Active Volume VIII include is missing: $chapter"
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
        throw "Volume VIII latexmk build failed with exit code $LASTEXITCODE"
    }

    $logPath = Join-Path $vol "book.log"
    if (-not (Test-Path -LiteralPath $logPath)) {
        throw "Volume VIII build completed without expected book.log."
    }

    $logText = [System.IO.File]::ReadAllText($logPath)
    foreach ($pattern in @(
        "LaTeX Warning: There were undefined references",
        "multiply defined",
        "There were undefined citations"
    )) {
        if ($logText.IndexOf($pattern, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
            throw "Volume VIII reference regression detected: $pattern"
        }
    }

    $pdf = Join-Path $vol "book.pdf"
    if (-not (Test-Path -LiteralPath $pdf)) {
        throw "Volume VIII PDF was not produced."
    }

    Write-Host ""
    Write-Host "VOLUME VIII BUILD PASSED" -ForegroundColor Green
    Write-Host ("Active chapters: " + $includes.Count)
    Write-Host ("PDF: " + $pdf)
}
finally {
    Pop-Location
}
