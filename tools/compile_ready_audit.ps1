param(
  [string]$CompileRoot = "imports/COMPILE_READY",
  [string]$BuildRoot = "build/compile-audit",
  [string]$ReportDir = "reports",
  [int]$TimeoutSeconds = 90
)

$ErrorActionPreference = "Stop"

$Repo = (Resolve-Path ".").Path
$CompileRootAbs = (Resolve-Path $CompileRoot).Path
$BuildRootAbs = Join-Path $Repo $BuildRoot
$ReportDirAbs = Join-Path $Repo $ReportDir
$RunRoot = Join-Path $BuildRootAbs "standalone"
$ProgressPath = Join-Path $BuildRootAbs "progress.txt"
$ResultsPath = Join-Path $ReportDirAbs "compile-audit-results.tsv"
$ReportPath = Join-Path $ReportDirAbs "compile-audit.md"

New-Item -ItemType Directory -Force -Path $BuildRootAbs | Out-Null
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
New-Item -ItemType Directory -Force -Path $ReportDirAbs | Out-Null

if (Test-Path -LiteralPath $ResultsPath) {
  Remove-Item -LiteralPath $ResultsPath -Force
}

$env:PATH = "C:\Program Files\Git\usr\bin;" + $env:PATH

function Get-Engine([string]$Text) {
  if ($Text -match "\\usepackage(?:\[[^\]]*\])?\{(?:fontspec|polyglossia|xeCJK)\}" -or
      $Text -match "\\setmainfont|\\setsansfont|\\setmonofont|\\newfontfamily") {
    return "xelatex"
  }
  return "pdflatex"
}

function Get-RepoRelativePath([string]$Path) {
  $full = [System.IO.Path]::GetFullPath($Path)
  $root = $Repo.TrimEnd("\", "/") + [System.IO.Path]::DirectorySeparatorChar
  if ($full.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) {
    return $full.Substring($root.Length)
  }
  return $full
}

function Get-FirstError([string]$LogPath, [string]$StdoutPath) {
  $sources = @()
  if (Test-Path -LiteralPath $LogPath) {
    $sources += Get-Content -LiteralPath $LogPath -ErrorAction SilentlyContinue
  }
  if ((-not $sources) -and (Test-Path -LiteralPath $StdoutPath)) {
    $sources += Get-Content -LiteralPath $StdoutPath -ErrorAction SilentlyContinue
  }
  foreach ($line in $sources) {
    if ($line -match "^! " -or
        $line -match "Fatal .* Error" -or
        $line -match "LaTeX Error:" -or
        $line -match "Package .* Error:" -or
        $line -match "^.+:\d+: .+") {
      return ($line.Trim() -replace "`t", " ")
    }
  }
  return ""
}

function Invoke-Latexmk([string]$TexFile, [string]$Engine, [string]$OutDir, [string]$StdoutPath, [int]$TimeoutSeconds) {
  $psi = New-Object System.Diagnostics.ProcessStartInfo
  $psi.FileName = "latexmk.exe"
  $psi.WorkingDirectory = $CompileRootAbs
  $psi.UseShellExecute = $false
  $psi.RedirectStandardOutput = $true
  $psi.RedirectStandardError = $true
  $psi.CreateNoWindow = $true
  $psi.Arguments = "-pdf -interaction=nonstopmode -halt-on-error -file-line-error -$Engine -outdir=`"$OutDir`" `"$TexFile`""
  $psi.Environment["PATH"] = $env:PATH

  $proc = New-Object System.Diagnostics.Process
  $proc.StartInfo = $psi
  [void]$proc.Start()

  $stdoutTask = $proc.StandardOutput.ReadToEndAsync()
  $stderrTask = $proc.StandardError.ReadToEndAsync()
  $finished = $proc.WaitForExit($TimeoutSeconds * 1000)
  if (-not $finished) {
    try { $proc.Kill($true) } catch { try { $proc.Kill() } catch {} }
    $stdout = $stdoutTask.GetAwaiter().GetResult()
    $stderr = $stderrTask.GetAwaiter().GetResult()
    Set-Content -LiteralPath $StdoutPath -Value ($stdout + "`n" + $stderr) -Encoding UTF8
    return @{ ExitCode = 124; TimedOut = $true }
  }
  $stdoutDone = $stdoutTask.GetAwaiter().GetResult()
  $stderrDone = $stderrTask.GetAwaiter().GetResult()
  Set-Content -LiteralPath $StdoutPath -Value ($stdoutDone + "`n" + $stderrDone) -Encoding UTF8
  return @{ ExitCode = $proc.ExitCode; TimedOut = $false }
}

$standalone = Get-ChildItem -LiteralPath $CompileRootAbs -File -Filter "*.tex" |
  Where-Object { (Get-Content -LiteralPath $_.FullName -Raw) -match "\\documentclass" } |
  Sort-Object Name

"file`tengine`tstatus`texit_code`ttimed_out`tpdf_path`terror`telapsed_seconds" | Set-Content -LiteralPath $ResultsPath -Encoding UTF8

$total = $standalone.Count
$i = 0
foreach ($tex in $standalone) {
  $i++
  $base = [System.IO.Path]::GetFileNameWithoutExtension($tex.Name)
  $outDir = Join-Path $RunRoot $base
  New-Item -ItemType Directory -Force -Path $outDir | Out-Null
  $text = Get-Content -LiteralPath $tex.FullName -Raw
  $engine = Get-Engine $text
  "[$i/$total] $($tex.Name) ($engine)" | Set-Content -LiteralPath $ProgressPath -Encoding UTF8

  $stdoutPath = Join-Path $outDir "$base.stdout.log"
  $started = Get-Date
  $run = Invoke-Latexmk $tex.Name $engine $outDir $stdoutPath $TimeoutSeconds
  $elapsed = [int]((Get-Date) - $started).TotalSeconds

  $pdf = Join-Path $outDir "$base.pdf"
  $log = Join-Path $outDir "$base.log"
  $status = if ($run.TimedOut) { "timeout" } elseif ($run.ExitCode -eq 0 -and (Test-Path -LiteralPath $pdf)) { "success" } else { "fail" }
  $err = Get-FirstError $log $stdoutPath
  $pdfRel = if (Test-Path -LiteralPath $pdf) { Get-RepoRelativePath $pdf } else { "" }
  $line = @($tex.Name, $engine, $status, $run.ExitCode, $run.TimedOut, $pdfRel, $err, $elapsed) -join "`t"
  Add-Content -LiteralPath $ResultsPath -Value $line -Encoding UTF8
}

"complete" | Set-Content -LiteralPath $ProgressPath -Encoding UTF8

$rows = Import-Csv -Path $ResultsPath -Delimiter "`t"
$success = @($rows | Where-Object { $_.status -eq "success" })
$fail = @($rows | Where-Object { $_.status -eq "fail" })
$timeout = @($rows | Where-Object { $_.status -eq "timeout" })
$fragments = @(Get-ChildItem -LiteralPath $CompileRootAbs -File -Filter "*.tex" |
  Where-Object { (Get-Content -LiteralPath $_.FullName -Raw) -notmatch "\\documentclass" } |
  Sort-Object Name)

$missingRefPath = Join-Path $CompileRootAbs "MISSING_REFERENCES.tsv"
$missingRefs = if (Test-Path -LiteralPath $missingRefPath) { @(Import-Csv -Path $missingRefPath -Delimiter "`t") } else { @() }

$report = New-Object System.Collections.Generic.List[string]
$report.Add("# Compile Audit") | Out-Null
$report.Add("") | Out-Null
$report.Add('- Compile root: `imports/COMPILE_READY`') | Out-Null
$report.Add('- Build root: `build/compile-audit/standalone`') | Out-Null
$report.Add('- Results table: `reports/compile-audit-results.tsv`') | Out-Null
$report.Add("- Standalone TeX tested: $($rows.Count)") | Out-Null
$report.Add("- Successful PDFs: $($success.Count)") | Out-Null
$report.Add("- Failed: $($fail.Count)") | Out-Null
$report.Add("- Timed out: $($timeout.Count)") | Out-Null
$report.Add("- Fragments not compiled directly: $($fragments.Count)") | Out-Null
$report.Add("- Missing unresolved figure references before compile: $($missingRefs.Count)") | Out-Null
$report.Add("") | Out-Null
$report.Add("## Successful PDFs") | Out-Null
$report.Add("") | Out-Null
foreach ($row in ($success | Sort-Object file)) {
  $report.Add(('- `{0}` -> `{1}`' -f $row.file, $row.pdf_path)) | Out-Null
}
$report.Add("") | Out-Null
$report.Add("## Failed Or Timed Out") | Out-Null
$report.Add("") | Out-Null
foreach ($row in (($fail + $timeout) | Sort-Object file)) {
  $report.Add(('- `{0}` [{1}, {2}, exit {3}]: {4}' -f $row.file, $row.engine, $row.status, $row.exit_code, $row.error)) | Out-Null
}
$report.Add("") | Out-Null
$report.Add("## Missing References") | Out-Null
$report.Add("") | Out-Null
if ($missingRefs.Count -eq 0) {
  $report.Add("None.") | Out-Null
} else {
  foreach ($ref in $missingRefs) {
    $report.Add(('- `{0}`: `{1}{{{2}}}`' -f $ref.file, $ref.command, $ref.reference)) | Out-Null
  }
}
$report.Add("") | Out-Null
$report.Add("## Fragments") | Out-Null
$report.Add("") | Out-Null
foreach ($frag in $fragments) {
  $report.Add(('- `{0}`' -f $frag.Name)) | Out-Null
}

Set-Content -LiteralPath $ReportPath -Value $report -Encoding UTF8
