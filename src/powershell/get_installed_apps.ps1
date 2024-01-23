[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |
    ConvertTo-Json
