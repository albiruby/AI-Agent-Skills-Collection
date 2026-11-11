[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Destination,

    [switch]$Overwrite
)

$ErrorActionPreference = 'Stop'
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceRoot = Join-Path $ScriptRoot 'skills'

if (-not (Test-Path -LiteralPath $SourceRoot -PathType Container)) {
    throw "Could not find package skills directory: $SourceRoot"
}

$DestinationPath = [System.IO.Path]::GetFullPath($Destination)
New-Item -ItemType Directory -Path $DestinationPath -Force | Out-Null
$Installed = 0
$Skipped = 0

Get-ChildItem -LiteralPath $SourceRoot -Directory | ForEach-Object {
    $SkillFolder = $_
    $Manifest = Join-Path $SkillFolder.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $Manifest -PathType Leaf)) { return }

    $Target = Join-Path $DestinationPath $SkillFolder.Name
    if (Test-Path -LiteralPath $Target) {
        if ($Overwrite) {
            Remove-Item -LiteralPath $Target -Recurse -Force
        }
        else {
            Write-Host "SKIP existing: $Target (use -Overwrite to replace)"
            $script:Skipped++
            return
        }
    }

    Copy-Item -LiteralPath $SkillFolder.FullName -Destination $Target -Recurse
    Write-Host "INSTALLED: $Target"
    $script:Installed++
}

Write-Host ""
Write-Host "Installed: $Installed"
Write-Host "Skipped: $Skipped"
Write-Host "Destination: $DestinationPath"
