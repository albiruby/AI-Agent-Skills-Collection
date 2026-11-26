# Repository-level checks beyond SKILL.md frontmatter.
# Verifies README pack counts, referenced paths, JSON validity, and local README links.
# Run locally: powershell -File .github/scripts/validate-repo.ps1

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$failures = @()

function Add-Failure($path, $msg) {
    $script:failures += "${path}: $msg"
}

# 1. README pack table counts and totals.
$readmePath = Join-Path $repoRoot 'README.md'
$readme = [IO.File]::ReadAllText($readmePath, [Text.Encoding]::UTF8)
$rows = [regex]::Matches($readme, '(?m)^\| \[`([^`]+)`\]\(([^)]+)\) \| (\d+)')
if ($rows.Count -eq 0) {
    Add-Failure 'README.md' 'no pack rows found in the Packs table'
}
$declaredTotal = 0
foreach ($m in $rows) {
    $name = $m.Groups[1].Value
    $link = $m.Groups[2].Value.TrimEnd('/')
    $declared = [int]$m.Groups[3].Value
    $declaredTotal += $declared
    $dir = Join-Path $repoRoot $link
    if (-not (Test-Path $dir -PathType Container)) {
        Add-Failure 'README.md' "pack link does not exist: $link"
        continue
    }
    $skills = Get-ChildItem -Path $dir -Recurse -Filter 'SKILL.md' -File | Where-Object {
        $_.Directory.Name -ne '_template' -and $_.FullName -notmatch '[\\/]templates[\\/]'
    }
    if ($skills.Count -ne $declared) {
        Add-Failure 'README.md' "pack '$name' declares $declared skills but contains $($skills.Count)"
    }
}
$badge = [regex]::Match($readme, 'skills-(\d+)-brightgreen')
if ($badge.Success -and [int]$badge.Groups[1].Value -ne $declaredTotal) {
    Add-Failure 'README.md' "skills badge says $($badge.Groups[1].Value) but pack rows total $declaredTotal"
}
$textCount = [regex]::Match($readme, '\*\*(\d+) skills\*\*')
if ($textCount.Success -and [int]$textCount.Groups[1].Value -ne $declaredTotal) {
    Add-Failure 'README.md' "summary says $($textCount.Groups[1].Value) skills but pack rows total $declaredTotal"
}

# 2. Referenced paths in every SKILL.md must exist relative to the skill folder.
$skillFiles = Get-ChildItem -Path $repoRoot -Recurse -Filter 'SKILL.md' -File | Where-Object {
    $_.Directory.Name -ne '_template' -and $_.FullName -notmatch '[\\/]templates[\\/]'
}
foreach ($file in $skillFiles) {
    $rel = $file.FullName.Substring($repoRoot.Length + 1) -replace '\\', '/'
    $raw = [IO.File]::ReadAllText($file.FullName, [Text.Encoding]::UTF8)
    $refs = [regex]::Matches($raw, '`((?:references|templates|adapters|examples|evals|scripts)/[^`\s]+)`')
    foreach ($r in $refs) {
        $target = $r.Groups[1].Value.TrimEnd('.', ',', ';', ':', ')', ']')
        $resolved = Join-Path $file.DirectoryName $target
        if (-not (Test-Path $resolved)) {
            Add-Failure $rel "referenced path does not exist: $target"
        }
    }
}

# 3. JSON files must parse.
$jsonFiles = Get-ChildItem -Path $repoRoot -Recurse -Filter '*.json' -File | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]'
}
foreach ($j in $jsonFiles) {
    try {
        [IO.File]::ReadAllText($j.FullName, [Text.Encoding]::UTF8) | ConvertFrom-Json | Out-Null
    } catch {
        Add-Failure ($j.FullName.Substring($repoRoot.Length + 1)) "invalid JSON: $($_.Exception.Message)"
    }
}

# 4. Local links in the root README must resolve.
foreach ($m in [regex]::Matches($readme, '\]\(([^)#]+)\)')) {
    $target = $m.Groups[1].Value
    if ($target -match '^(https?:|mailto:|#)') { continue }
    $target = $target.Split('#')[0]
    $resolved = Join-Path $repoRoot $target
    if (-not (Test-Path $resolved)) {
        Add-Failure 'README.md' "local link does not resolve: $target"
    }
}

Write-Host "Checked $($rows.Count) pack row(s), $($skillFiles.Count) SKILL.md file(s), $($jsonFiles.Count) JSON file(s)."
if ($failures.Count -gt 0) {
    Write-Host "`nFAIL: $($failures.Count) violation(s):" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    exit 1
}
Write-Host 'Repository checks passed.' -ForegroundColor Green
exit 0
