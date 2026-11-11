# Validates every SKILL.md in this repository against the house conventions.
# Run locally:  powershell -File .github/scripts/validate-frontmatter.ps1
# Exits non-zero (and fails CI) on the first class of violations found.

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$failures = @()
$checked = 0

# Files that are intentionally not skills.
$excludedFiles = @('SKILL_TEMPLATE.md')

function Add-Failure($path, $msg) {
    $script:failures += "${path}: $msg"
}

$skillFiles = Get-ChildItem -Path $repoRoot -Recurse -Filter 'SKILL.md' -File |
    Where-Object {
        $relPath = ($_.FullName.Substring($repoRoot.Length + 1) -replace '\\', '/')
        $excludedFiles -notcontains $_.Name -and
        $relPath -notmatch '(^|/)_template/' -and
        $relPath -notmatch '(^|/)templates/'
    }

foreach ($file in $skillFiles) {
    $checked++
    $rel = $file.FullName.Substring($repoRoot.Length + 1) -replace '\\', '/'

    $raw = [IO.File]::ReadAllText($file.FullName)
    $lines = $raw -split "`r?`n"

    # 1. Frontmatter block at the very top.
    if ($lines[0] -ne '---') {
        Add-Failure $rel 'file must start with YAML frontmatter (---)'
        continue
    }
    $closeIdx = -1
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -eq '---') { $closeIdx = $i; break }
    }
    if ($closeIdx -lt 0) {
        Add-Failure $rel 'frontmatter is never closed with ---'
        continue
    }
    $frontmatter = $lines[1..($closeIdx - 1)]

    # 2. Exactly two keys: name and description.
    $keys = @()
    foreach ($line in $frontmatter) {
        if ($line -match '^([A-Za-z_-]+)\s*:') { $keys += $Matches[1] }
        elseif ($line -match '^\s*\S' -and $line -notmatch '^\s*#') {
            # continuation line of a folded/multiline value is fine
        }
    }
    $extra = $keys | Where-Object { $_ -notin 'name', 'description' }
    $missing = @('name', 'description') | Where-Object { $_ -notin $keys }
    if ($missing.Count -gt 0) { Add-Failure $rel ("missing frontmatter key(s): " + ($missing -join ', ')) }
    if ($extra.Count -gt 0) { Add-Failure $rel ("extra frontmatter key(s) not allowed: " + ($extra -join ', ')) }

    # 3. name is present, non-empty, kebab-case, and equals the folder name.
    $name = ''
    foreach ($line in $frontmatter) {
        if ($line -match '^name\s*:\s*(.+)$') { $name = $Matches[1].Trim().Trim('"', "'"); break }
    }
    if ($name -eq '') {
        Add-Failure $rel 'name is empty'
    } else {
        if ($name -notmatch '^[a-z0-9]+(-[a-z0-9]+)*$') {
            Add-Failure $rel "name '$name' must be kebab-case (a-z, 0-9, hyphens)"
        }
        $folder = $file.Directory.Name
        if ($folder -ne $name) {
            Add-Failure $rel "folder '$folder' must equal name '$name'"
        }
    }

    # 4. description present, under 1024 chars, with an explicit trigger.
    $desc = ''
    foreach ($line in $frontmatter) {
        if ($line -match '^description\s*:\s*(.*)$') { $desc = $Matches[1].Trim().Trim('"', "'"); break }
    }
    if ($desc -eq '') {
        Add-Failure $rel 'description is empty'
    } else {
        if ($desc.Length -gt 1024) {
            Add-Failure $rel "description is $($desc.Length) chars (max 1024)"
        }
        if ($desc -notmatch '(?i)\buse (when|whenever)\b') {
            Add-Failure $rel "description lacks a 'Use when...' trigger"
        }
    }

    # 5. First H1 is the file title: present, not a placeholder, not ALL CAPS.
    #    (Body sections may repeat "# ..." — packs differ on H1 vs H2 sections;
    #    consistency is per-pack, so only the title line is enforced.)
    $h1s = @()
    $fence = $false
    foreach ($line in $lines) {
        if ($line -match '^\s*```') { $fence = -not $fence; continue }
        if (-not $fence -and $line -match '^#\s+\S') { $h1s += $line }
    }
    if ($h1s.Count -eq 0) {
        Add-Failure $rel 'missing H1 title'
    } else {
        $title = $h1s[0]
        if ($title -match '^#\s+(Instructions|Skill\s*:|Title\s*$)') {
            Add-Failure $rel "placeholder H1: '$title'"
        }
        if ($title -cmatch '^#\s+[A-Z0-9\s&:()\-]{6,}$' -and $title -cmatch '^[A-Z0-9\s&:()\-]+$') {
            Add-Failure $rel "H1 title must be title case, not ALL CAPS: '$title'"
        }
    }
}

# 6. No stale artifacts.
$junk = Get-ChildItem -Path $repoRoot -Recurse -Force -Directory |
    Where-Object { $_.Name -eq '__pycache__' -or $_.FullName -match '\\\.git\\' -and $_.Name -ne '.git' }
$pyc = Get-ChildItem -Path $repoRoot -Recurse -Force -File -Include '*.pyc', '*.pyo' -ErrorAction SilentlyContinue
foreach ($j in $junk) {
    if ($j.FullName -match '\\\.git\\') { continue }
    Add-Failure ($j.FullName.Substring($repoRoot.Length + 1)) 'junk directory must not be committed'
}
foreach ($p in $pyc) { Add-Failure $p.Name 'compiled Python cache must not be committed' }

Write-Host "Checked $checked SKILL.md file(s)."
if ($failures.Count -gt 0) {
    Write-Host "`nFAIL: $($failures.Count) violation(s):" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    exit 1
}
Write-Host 'All checks passed.' -ForegroundColor Green
exit 0
