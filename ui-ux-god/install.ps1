param(
    [Parameter(Mandatory=$true)]
    [string]$Destination,
    [switch]$Overwrite
)

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PackName = Split-Path $ScriptDir -Leaf

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
$Destination = (Resolve-Path $Destination).Path
$Target = Join-Path $Destination $PackName

if ((Resolve-Path $ScriptDir).Path -eq $Target) {
    Write-Host "Source and destination are the same: $Target"
    exit 0
}

if (Test-Path $Target) {
    if (-not $Overwrite) {
        Write-Host "SKIP    $PackName (already exists at $Target; use -Overwrite to replace)"
        exit 0
    }
    Remove-Item -Recurse -Force $Target
}

Write-Host "INSTALL $PackName -> $Target"
Copy-Item -Recurse -Force $ScriptDir $Target

# Remove local-only artifacts from the installed copy.
foreach ($junk in @('__pycache__', 'node_modules', 'audit-out', '.git')) {
    Get-ChildItem -Path $Target -Recurse -Force -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -eq $junk } |
        ForEach-Object { Remove-Item -Recurse -Force $_.FullName }
}

$skillCount = (Get-ChildItem -Path (Join-Path $Target 'skills') -Recurse -Filter 'SKILL.md' -File).Count
Write-Host "Done. Installed $skillCount skills."
Write-Host "Validate with: python `"$Target\scripts\validate_package.py`""
