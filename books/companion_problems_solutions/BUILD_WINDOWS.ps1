param(
    [Parameter(Mandatory=$false)][string]$Repo = (Get-Location).Path,
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$Repo = (Resolve-Path $Repo).Path
$BookDir = Join-Path $Repo "books\companion_problems_solutions"
$ScriptDir = Join-Path $Repo "scripts\companion"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "python not found on PATH" }
if (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) { throw "latexmk not found on PATH" }

function Invoke-PythonValidator {
    param(
        [Parameter(Mandatory=$true)][string]$Path,
        [Parameter(Mandatory=$true)][string]$Label
    )

    if (-not (Test-Path $Path)) {
        throw "Missing validator: $Path"
    }

    Write-Host ""
    Write-Host "=== $Label ==="
    & python $Path --repo $Repo
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed."
    }
}

# 1. Permanent structure/schema gate.
Invoke-PythonValidator `
    -Path (Join-Path $ScriptDir "validate_companion_scaffold.py") `
    -Label "Companion structure validation"

# 2. Semantic atlas gate, once the atlas classifier exists.
$AtlasValidator = Join-Path $ScriptDir "validate_companion_problem_atlas.py"
if (Test-Path $AtlasValidator) {
    Invoke-PythonValidator `
        -Path $AtlasValidator `
        -Label "Companion semantic atlas validation"
}

# 3. Every migrated Part validator currently present.
$PartValidators = @(
    Get-ChildItem `
        -Path $ScriptDir `
        -Filter "validate_companion_part*.py" `
        -File `
        -ErrorAction SilentlyContinue |
    Sort-Object Name
)

foreach ($Validator in $PartValidators) {
    Invoke-PythonValidator `
        -Path $Validator.FullName `
        -Label ("Companion migrated-Part validation: " + $Validator.Name)
}

if ($Clean) {
    Push-Location $BookDir
    try {
        latexmk -C book.tex | Out-Host
        if ($LASTEXITCODE -ne 0) { throw "latexmk clean failed." }
    }
    finally {
        Pop-Location
    }
}

Write-Host ""
Write-Host "=== Companion PDF build ==="

Push-Location $BookDir
try {
    latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex | Out-Host
    if ($LASTEXITCODE -ne 0) { throw "latexmk failed." }
}
finally {
    Pop-Location
}

$pdf = Join-Path $BookDir "book.pdf"
if (-not (Test-Path $pdf)) { throw "Expected PDF not produced: $pdf" }

Write-Host ""
Write-Host "Companion build passed: $pdf"
