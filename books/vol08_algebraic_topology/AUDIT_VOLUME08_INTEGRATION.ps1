param(
  [Parameter(Mandatory=$true)][string]$Repo,
  [switch]$WriteReports
)
$ErrorActionPreference = "Stop"
$Repo = (Resolve-Path $Repo).Path
$Vol = Join-Path $Repo "books/vol08_algebraic_topology"
$Book = Join-Path $Vol "book.tex"
$StatusPath = Join-Path $Repo "editorial/CHAPTER_STATUS.tsv"

function ReadText([string]$p) {
  return [System.IO.File]::ReadAllText($p)
}

$chapterFiles = @(Get-ChildItem (Join-Path $Vol "chapters") -Directory |
  Where-Object { $_.Name -match '^ch\d\d_' } |
  ForEach-Object { Join-Path $_.FullName "chapter.tex" } |
  Where-Object { Test-Path $_ } |
  Sort-Object)

$bookText = ReadText $Book
$includes = @([regex]::Matches($bookText, '\\include\{chapters/ch\d\d_[^}]+/chapter\}'))
$labels = @()
$refs = @()
$problemRows = @()

foreach ($cf in $chapterFiles) {
  $t = ReadText $cf
  foreach ($m in [regex]::Matches($t, '\\label\{([^}]+)\}')) {
    $labels += $m.Groups[1].Value
  }
  foreach ($m in [regex]::Matches($t, '\\(?:ref|eqref|autoref)\{([^}]+)\}')) {
    $refs += $m.Groups[1].Value
  }
  $pr = ([regex]::Matches($t,'\\begin\{problem\}')).Count
  $so = ([regex]::Matches($t,'\\begin\{solution\}')).Count
  $problemRows += [pscustomobject]@{
    Chapter = Split-Path (Split-Path $cf -Parent) -Leaf
    Problems = $pr
    Solutions = $so
    Balanced = ($pr -eq $so)
  }
}

$dups = @($labels | Group-Object | Where-Object Count -gt 1 | Sort-Object Name)
$labelSet = @{}
foreach ($l in $labels) { $labelSet[$l] = $true }
$missingInternal = @($refs | Sort-Object -Unique | Where-Object {
  ($_ -match 'viii\d\d') -and (-not $labelSet.ContainsKey($_))
})

$svgFiles = @(Get-ChildItem (Join-Path $Vol "figures") -Recurse -File -Filter *.svg -ErrorAction SilentlyContinue | Sort-Object FullName)
$svgWarnings = @()
foreach ($svg in $svgFiles) {
  $s = ReadText $svg.FullName
  $missing = @()
  if ($s -notmatch '<title(?:\s|>)') { $missing += "title" }
  if ($s -notmatch '<desc(?:\s|>)') { $missing += "desc" }
  if ($s -notmatch 'viewBox=') { $missing += "viewBox" }
  if ($missing.Count -gt 0) {
    $svgWarnings += [pscustomobject]@{
      Path = $svg.FullName.Substring($Repo.Length+1).Replace('\','/')
      Missing = ($missing -join ", ")
    }
  }
}

$status = Get-Content -LiteralPath $StatusPath
$viiiRows = @($status | Where-Object { $_ -like "VIII`tVIII/*" })

$blocking = @()
if ($chapterFiles.Count -ne 35) { $blocking += "Expected 35 chapter files, found $($chapterFiles.Count)." }
if ($includes.Count -ne 35) { $blocking += "Expected 35 active chapter includes, found $($includes.Count)." }
if ($viiiRows.Count -ne 35) { $blocking += "Expected 35 VIII status rows, found $($viiiRows.Count)." }
if ($dups.Count -gt 0) { $blocking += "Duplicate labels: $($dups.Count)." }
$unbalanced = @($problemRows | Where-Object { -not $_.Balanced })
if ($missingInternal.Count -gt 0) { $blocking += "Missing Volume-VIII internal references: $($missingInternal.Count)." }

if ($WriteReports) {
  $inv = @()
  $inv += "# Volume VIII — SVG Inventory"
  $inv += ""
  $inv += "Tracked editable SVG source assets discovered under books/vol08_algebraic_topology/figures."
  $inv += ""
  $inv += "**Total SVG assets:** $($svgFiles.Count)"
  $inv += ""
  foreach ($svg in $svgFiles) {
    $rel = $svg.FullName.Substring($Vol.Length+1).Replace('\','/')
    $inv += "- $rel"
  }
  $inv += ""
  $inv += "## Metadata warnings"
  if ($svgWarnings.Count -eq 0) {
    $inv += "None."
  } else {
    foreach ($w in $svgWarnings) { $inv += "- $($w.Path): missing $($w.Missing)" }
  }
  [System.IO.File]::WriteAllText((Join-Path $Vol "VOLUME08_SVG_INVENTORY.md"),
    (($inv -join "`n").TrimEnd() + "`n"), (New-Object System.Text.UTF8Encoding($false)))

  $rep = @()
  $rep += "# Volume VIII — Integration Audit"
  $rep += ""
  $rep += "- Canonical chapter files: **$($chapterFiles.Count)**"
  $rep += "- Active chapter includes: **$($includes.Count)**"
  $rep += "- Volume VIII status rows: **$($viiiRows.Count)**"
  $rep += "- Unique labels: **$($labels.Count)**"
  $rep += "- Duplicate labels: **$($dups.Count)**"
  $rep += "- Missing Volume-VIII internal refs: **$($missingInternal.Count)**"
  $rep += "- SVG assets: **$($svgFiles.Count)**"
  $rep += "- SVG metadata warnings: **$($svgWarnings.Count)**"
  $rep += "- Unbalanced Problem/Solution chapters (reported, not frozen here): **$($unbalanced.Count)**"
  $rep += ""
  $rep += "## Problem/Solution balance"
  foreach ($r in $problemRows) {
    $rep += "- $($r.Chapter): $($r.Problems) problems / $($r.Solutions) solutions"
  }
  $rep += ""
  $rep += "## Blocking structural findings"
  if ($blocking.Count -eq 0) { $rep += "None." } else { foreach ($b in $blocking) { $rep += "- $b" } }
  $rep += ""
  $rep += "## Deliberately not certified here"
  $rep += "The legacy one-to-one dossier/problem/solution/provenance/figure reconciliation remains pending."
  [System.IO.File]::WriteAllText((Join-Path $Vol "VOLUME08_INTEGRATION_AUDIT.md"),
    (($rep -join "`n").TrimEnd() + "`n"), (New-Object System.Text.UTF8Encoding($false)))
}

if ($blocking.Count -gt 0) {
  $blocking | ForEach-Object { Write-Host "BLOCK: $_" }
  exit 2
}

Write-Host "Volume VIII integration audit passed:"
Write-Host "  chapters=$($chapterFiles.Count) includes=$($includes.Count) status_rows=$($viiiRows.Count)"
Write-Host "  labels=$($labels.Count) svg=$($svgFiles.Count) svg_metadata_warnings=$($svgWarnings.Count)"
