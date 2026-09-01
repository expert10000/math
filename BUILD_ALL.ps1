param(
    [switch]$CanonicalOnly,
    [switch]$CleanFirst,
    [switch]$FailFast,
    [switch]$NoPdfCollection,
    [switch]$AllowFailures,
    [string]$InventoryPath = ""
)
$ErrorActionPreference = "Stop"
$Repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$Books = Join-Path $Repo "books"
$CollectedPdfDir = Join-Path $Repo "build\pdf"
if ([string]::IsNullOrWhiteSpace($InventoryPath)) {
    $InventoryPath = Join-Path $Repo "reports\series\BUILD_I_VIII.tsv"
}
if (-not (Test-Path (Join-Path $Repo ".git"))) { throw "BUILD_ALL.ps1 must be stored in the repository root." }
if (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) { throw "latexmk is not available on PATH." }
if (-not $NoPdfCollection) { New-Item -ItemType Directory -Force -Path $CollectedPdfDir | Out-Null }
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $InventoryPath) | Out-Null

$roman = @("I","II","III","IV","V","VI","VII","VIII")
$volumeDirs = @(Get-ChildItem -Path $Books -Directory | Where-Object { $_.Name -match '^vol0[1-8]_' } | Sort-Object Name)
$inventory = New-Object System.Collections.Generic.List[object]
$targets = New-Object System.Collections.Generic.List[object]

foreach ($vol in $volumeDirs) {
    $m=[regex]::Match($vol.Name,'^vol(\d\d)_')
    $n=[int]$m.Groups[1].Value
    $v=$roman[$n-1]
    $book=Join-Path $vol.FullName "book.tex"
    if (Test-Path $book) {
        $targets.Add([pscustomobject]@{ Volume=$v; VolumeDir=$vol.Name; File="book.tex"; Kind="canonical"; Dir=$vol.FullName })
    } else {
        $inventory.Add([pscustomobject]@{ volume=$v; volume_dir=$vol.Name; target="book.tex"; kind="canonical";
            status="NO_WRAPPER"; pdf="N/A"; bytes="N/A"; sha256="N/A"; error="Canonical book.tex not yet created" })
    }
    if (-not $CanonicalOnly) {
        foreach ($pattern in @("part*_student.tex","part*_hints.tex","part*_complete.tex")) {
            Get-ChildItem -Path $vol.FullName -File -Filter $pattern -ErrorAction SilentlyContinue | Sort-Object Name | ForEach-Object {
                $targets.Add([pscustomobject]@{ Volume=$v; VolumeDir=$vol.Name; File=$_.Name; Kind="edition"; Dir=$vol.FullName })
            }
        }
    }
}

$failed=0
foreach ($target in $targets) {
    Write-Host "============================================================" -ForegroundColor DarkGray
    Write-Host "BUILD: Volume $($target.Volume) / $($target.File)" -ForegroundColor Cyan
    Push-Location $target.Dir
    try {
        if ($CleanFirst) {
            & latexmk -C $target.File
            if ($LASTEXITCODE -ne 0) { throw "latexmk clean failed ($LASTEXITCODE)" }
        }
        & latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error $target.File
        if ($LASTEXITCODE -ne 0) { throw "latexmk failed ($LASTEXITCODE)" }
        $pdfName=[System.IO.Path]::ChangeExtension($target.File,".pdf")
        $pdfPath=Join-Path $target.Dir $pdfName
        if (-not (Test-Path $pdfPath)) { throw "PDF missing after successful latexmk: $pdfPath" }
        $hash=(Get-FileHash -Algorithm SHA256 -LiteralPath $pdfPath).Hash.ToLowerInvariant()
        $item=Get-Item $pdfPath
        if (-not $NoPdfCollection) {
            Copy-Item -Force $pdfPath (Join-Path $CollectedPdfDir "$($target.VolumeDir)_$([IO.Path]::GetFileNameWithoutExtension($target.File)).pdf")
        }
        $inventory.Add([pscustomobject]@{ volume=$target.Volume; volume_dir=$target.VolumeDir; target=$target.File; kind=$target.Kind;
            status="PASS"; pdf=$pdfPath.Substring($Repo.Length+1).Replace('\','/'); bytes=$item.Length; sha256=$hash; error="-" })
        Write-Host "PASS: $pdfName" -ForegroundColor Green
    } catch {
        $failed++
        $inventory.Add([pscustomobject]@{ volume=$target.Volume; volume_dir=$target.VolumeDir; target=$target.File; kind=$target.Kind;
            status="FAIL"; pdf="N/A"; bytes="N/A"; sha256="N/A"; error=$_.Exception.Message })
        Write-Host "FAIL: $($_.Exception.Message)" -ForegroundColor Red
        if ($FailFast) { throw }
    } finally { Pop-Location }
}

# Deterministic TSV inventory.
$header="volume`tvolume_dir`ttarget`tkind`tstatus`tpdf`tbytes`tsha256`terror"
$lines=@($header)
foreach ($r in ($inventory | Sort-Object volume_dir,target)) {
    $err=($r.error -replace "`t"," " -replace "`r?`n"," ")
    $lines += "$($r.volume)`t$($r.volume_dir)`t$($r.target)`t$($r.kind)`t$($r.status)`t$($r.pdf)`t$($r.bytes)`t$($r.sha256)`t$err"
}
[System.IO.File]::WriteAllText($InventoryPath,(($lines -join "`n").TrimEnd()+"`n"),(New-Object System.Text.UTF8Encoding($false)))

# Human summary.
$md=Join-Path (Split-Path -Parent $InventoryPath) "BUILD_I_VIII.md"
$pass=@($inventory | Where-Object status -eq "PASS").Count
$fail=@($inventory | Where-Object status -eq "FAIL").Count
$no=@($inventory | Where-Object status -eq "NO_WRAPPER").Count
$body=@("# I-VIII Canonical Build Inventory","",
       "- PASS: **$pass**","- FAIL: **$fail**","- NO_WRAPPER: **$no**","",
       "| Volume | Target | Status | Detail |","|---|---|---|---|")
foreach ($r in ($inventory | Sort-Object volume_dir,target)) {
    $detail=if ($r.status -eq "PASS") { $r.pdf } else { $r.error }
    $detail=$detail.Replace("|","\|")
    $body += "| $($r.volume) | $($r.target) | $($r.status) | $detail |"
}
[System.IO.File]::WriteAllText($md,(($body -join "`n").TrimEnd()+"`n"),(New-Object System.Text.UTF8Encoding($false)))

Write-Host ""
Write-Host "SERIES BUILD SUMMARY" -ForegroundColor Cyan
Write-Host "PASS=$pass FAIL=$fail NO_WRAPPER=$no"
Write-Host "Inventory: $InventoryPath"
if ($failed -gt 0 -and -not $AllowFailures) { exit 1 }
exit 0
