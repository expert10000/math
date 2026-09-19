param(
    [Parameter(Mandatory=$false)][string]$Repo = (Get-Location).Path,
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$Repo = (Resolve-Path $Repo).Path
$BookDir = Join-Path $Repo "books\companion_problems_solutions"
$Validator = Join-Path $Repo "scripts\companion\validate_companion_scaffold.py"

if (-not (Test-Path $Validator)) { throw "Missing validator: $Validator" }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "python not found on PATH" }
if (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) { throw "latexmk not found on PATH" }

python $Validator --repo $Repo
if ($LASTEXITCODE -ne 0) { throw "Companion scaffold validation failed." }

if ($Clean) {
    Push-Location $BookDir
    try { latexmk -C book.tex | Out-Host }
    finally { Pop-Location }
}

Push-Location $BookDir
try {
    latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex | Out-Host
    if ($LASTEXITCODE -ne 0) { throw "latexmk failed." }
}
finally { Pop-Location }

$pdf = Join-Path $BookDir "book.pdf"
if (-not (Test-Path $pdf)) { throw "Expected PDF not produced: $pdf" }
Write-Host "Companion build passed: $pdf"
