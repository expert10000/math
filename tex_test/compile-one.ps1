param(
  [Parameter(Mandatory=$true)]
  [string]$File,
  [string]$Engine = "pdflatex"
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$texTestRoot = Resolve-Path -LiteralPath $scriptDir
$buildDir = Join-Path $texTestRoot "build"
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

$inputPath = Join-Path $texTestRoot $File
if (-not (Test-Path -LiteralPath $inputPath)) {
  throw "TeX file not found inside tex_test: $File"
}

Push-Location $texTestRoot
try {
  & $Engine -interaction=nonstopmode -halt-on-error -output-directory "$buildDir" "$File"
  exit $LASTEXITCODE
}
finally {
  Pop-Location
}
