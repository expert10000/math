param(
  [string]$Engine = "pdflatex",
  [string]$OutputDirectory,
  [int]$MaxFiles = 0
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceRoot = Resolve-Path -LiteralPath $scriptDir
$repoRoot = Resolve-Path -LiteralPath (Join-Path $sourceRoot "..")

if (-not $OutputDirectory) {
  $OutputDirectory = Join-Path $repoRoot "pdfs\chapters"
}

if ([System.IO.Path]::IsPathRooted($OutputDirectory)) {
  $outputDir = $OutputDirectory
}
else {
  $outputDir = Join-Path (Get-Location) $OutputDirectory
}

$outputDir = [System.IO.Path]::GetFullPath($outputDir)
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$reportPath = Join-Path $outputDir "compile-report.tsv"
$files = @(Get-ChildItem -LiteralPath (Join-Path $sourceRoot "tex") -Filter *.tex -File | Sort-Object Name)
if ($MaxFiles -gt 0) {
  $files = @($files | Select-Object -First $MaxFiles)
}

$rows = New-Object System.Collections.Generic.List[string]
$rows.Add((@("file", "status", "exit_code", "pdf") -join "`t"))

Push-Location $sourceRoot
try {
  foreach ($file in $files) {
    $relative = "tex\$($file.Name)"
    $pdfName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name) + ".pdf"
    $pdfPath = Join-Path $outputDir $pdfName

    & $Engine -interaction=nonstopmode -halt-on-error -output-directory "$outputDir" "$relative" | Out-Null
    $exitCode = $LASTEXITCODE
    $status = "failed"
    if ($exitCode -eq 0 -and (Test-Path -LiteralPath $pdfPath)) {
      $status = "ok"
    }

    $rows.Add((@($relative, $status, $exitCode, $pdfPath) -join "`t"))
    Set-Content -LiteralPath $reportPath -Value $rows -Encoding UTF8
  }
}
finally {
  Pop-Location
}

$ok = @($rows | Select-Object -Skip 1 | Where-Object { $_ -match "`tok`t" }).Count
$failed = @($rows | Select-Object -Skip 1 | Where-Object { $_ -match "`tfailed`t" }).Count
Write-Host "Compile report: $reportPath"
Write-Host "OK: $ok"
Write-Host "Failed: $failed"
if ($failed -gt 0) {
  exit 1
}
