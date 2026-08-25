param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "C:\Users\janko\Documents\MATH\math"
)

$ErrorActionPreference = "Stop"
$vol = Join-Path $Repo "books/vol06_algebraic_geometry"
if (-not (Test-Path (Join-Path $vol "book_full_solutions.tex"))) {
    throw "Missing full-solutions wrapper in $vol"
}

Push-Location $vol
try {
    & latexmk -C book_full_solutions.tex
    & latexmk -pdf -interaction=nonstopmode -halt-on-error book_full_solutions.tex
    if ($LASTEXITCODE -ne 0) { throw "latexmk full-solutions build failed with exit code $LASTEXITCODE" }
    Write-Host ""
    Write-Host "Full-solutions PDF built:"
    Write-Host (Join-Path $vol "book_full_solutions.pdf")
}
finally {
    Pop-Location
}
