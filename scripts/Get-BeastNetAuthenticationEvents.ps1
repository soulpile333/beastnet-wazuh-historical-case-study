<#
.SYNOPSIS
    Collect selected Windows authentication events from an authorized system.

.DESCRIPTION
    Reconstructed portfolio example based on the historical BeastNet workflow.
    This is not an original retained artifact. The CSV output may contain
    sensitive security-event data and is excluded from source control.

    Remote queries are limited to systems the caller is authorized to access.
    The default 24-hour window can be extended to 30 days (720 hours) when
    the authorized system and collection purpose support that range.

.PARAMETER ComputerName
    Authorized local or remote Windows computer to query.

.PARAMETER Hours
    Number of hours to search, from 1 through 720. Defaults to 24.

.PARAMETER OutputPath
    CSV path. Its parent directory is created when needed.
#>
[CmdletBinding()]
param(
    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$ComputerName = $env:COMPUTERNAME,

    [Parameter()]
    [ValidateRange(1, 720)]
    [int]$Hours = 24,

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$OutputPath = ".\AuthenticationEvents.csv"
)

Set-StrictMode -Version Latest

$eventNames = @{
    4624 = "Successful logon"
    4625 = "Failed logon"
    4740 = "Account lockout"
}

$outputFile = [System.IO.Path]::GetFullPath($OutputPath)
$outputDirectory = Split-Path -Path $outputFile -Parent

if (-not (Test-Path -LiteralPath $outputDirectory -PathType Container)) {
    New-Item -Path $outputDirectory -ItemType Directory -Force -ErrorAction Stop | Out-Null
}

$filter = @{
    LogName   = "Security"
    Id        = 4624, 4625, 4740
    StartTime = (Get-Date).AddHours(-$Hours)
}

try {
    Get-WinEvent -ComputerName $ComputerName -FilterHashtable $filter -ErrorAction Stop |
        Select-Object TimeCreated, MachineName, Id,
            @{Name = "EventDescription"; Expression = {
                $eventNames[[int]$_.Id]
            }},
            RecordId, Message |
        Export-Csv -Path $outputFile -NoTypeInformation -ErrorAction Stop

    Write-Host "Events exported to $outputFile" -ForegroundColor Green
}
catch {
    Write-Error (
        "Query or export failed. Verify authorization, DNS, firewall rules, " +
        "permissions, Remote Event Log Management, and output access. " +
        $_.Exception.Message
    )
}
