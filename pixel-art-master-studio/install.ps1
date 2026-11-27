param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Destination,
    [switch]$Overwrite
)

$ErrorActionPreference = 'Stop'
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceRoot = Join-Path $ScriptRoot 'skills'

if (-not (Test-Path -LiteralPath $SourceRoot -PathType Container)) {
    throw "Skills source directory not found: $SourceRoot"
}

$DestinationPath = [System.IO.Path]::GetFullPath($Destination)
New-Item -ItemType Directory -Force -Path $DestinationPath | Out-Null
$Installed = 0
$Skipped = 0

Get-ChildItem -LiteralPath $SourceRoot -Directory | ForEach-Object {
    $SkillName = $_.Name
    $Target = Join-Path $DestinationPath $SkillName
    if (Test-Path -LiteralPath $Target) {
        if ($Overwrite) {
            Remove-Item -LiteralPath $Target -Recurse -Force
        }
        else {
            Write-Host "SKIP  $SkillName (already exists)"
            $Skipped++
            return
        }
    }
    Copy-Item -LiteralPath $_.FullName -Destination $Target -Recurse
    $SkillFile = Join-Path $Target 'SKILL.md'
    if (-not (Test-Path -LiteralPath $SkillFile -PathType Leaf)) {
        throw "SKILL.md missing after copy: $SkillName"
    }
    Write-Host "OK    $SkillName"
    $Installed++
}

Write-Host "Installed: $Installed | Skipped: $Skipped | Destination: $DestinationPath"
