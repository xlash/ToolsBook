param([String]$sensitiveArg)

function Test-ScriptBlocking
{
    $basePath = “VERY_SENSITIVE_INFO”

    if(-not (Test-Path $basePath))
    {
        $null = New-Item $basePath -Force
    }
    Write-Output $basePath $sensitiveArg
}

Test-ScriptBlocking