param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Destination,
    [switch]$Overwrite
)
$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
$Installed = 0
$Skipped = 0
Get-ChildItem -Path $ScriptDir -Directory | ForEach-Object {
    $SkillDir = $_
    $SkillFile = Join-Path $SkillDir.FullName 'SKILL.md'
    if (Test-Path $SkillFile) {
        $Target = Join-Path $Destination $SkillDir.Name
        if ((Test-Path $Target) -and -not $Overwrite) {
            Write-Host "SKIP existing: $($SkillDir.Name)"
            $Skipped++
        } else {
            if (Test-Path $Target) { Remove-Item -Recurse -Force $Target }
            Copy-Item -Recurse -Force $SkillDir.FullName $Target
            Write-Host "INSTALLED: $($SkillDir.Name)"
            $Installed++
        }
    }
}
Write-Host "Done. Installed: $Installed | Skipped: $Skipped | Destination: $Destination"
