param(
    [Parameter(Mandatory=$false)]
    [string]$Repo = "C:\Users\janko\Documents\MATH\math",

    [switch]$Clean
)

$ErrorActionPreference = "Stop"

$vol = Join-Path $Repo "books/vol07_differential_geometry"
$book = Join-Path $vol "book.tex"

if (-not (Test-Path $book)) {
    throw "Missing Volume VII wrapper: $book"
}

$required = @(
    "chapters/ch01_topological_manifolds/chapter.tex",
    "chapters/ch02_smooth_structures_and_atlases/chapter.tex",
    "chapters/ch03_smooth_maps_and_diffeomorphisms/chapter.tex"
)

foreach ($rel in $required) {
    $path = Join-Path $vol $rel
    if (-not (Test-Path $path)) {
        throw "Missing reconstructed Volume VII chapter: $path"
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

    Write-Host ""
    Write-Host "VOLUME VII BUILD PASSED" -ForegroundColor Green
    Write-Host ("PDF: " + (Join-Path $vol "book.pdf"))
}
finally {
    Pop-Location
}
