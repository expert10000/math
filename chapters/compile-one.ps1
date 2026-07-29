param(
  [Parameter(Mandatory=$true)]
  [string]$File,
  [string]$Engine = "pdflatex",
  [string]$OutputDirectory
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceRoot = Resolve-Path -LiteralPath $scriptDir
$repoRoot = Resolve-Path -LiteralPath (Join-Path $sourceRoot "..")

if (-not $OutputDirectory) {
  $OutputDirectory = Join-Path $repoRoot "content"
}

if ([System.IO.Path]::IsPathRooted($OutputDirectory)) {
  $outputDir = $OutputDirectory
}
else {
  $outputDir = Join-Path (Get-Location) $OutputDirectory
}

$outputDir = [System.IO.Path]::GetFullPath($outputDir)
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$inputPath = Join-Path $sourceRoot $File
if (-not (Test-Path -LiteralPath $inputPath)) {
  throw "TeX file not found inside chapters folder: $File"
}

Push-Location $sourceRoot
try {
  & $Engine -interaction=nonstopmode -halt-on-error -output-directory "$outputDir" "$File"
  exit $LASTEXITCODE
}
finally {
  Pop-Location
}
