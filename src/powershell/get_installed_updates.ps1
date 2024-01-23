[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Get-HotFix | Select-Object -Property Description, HotFixID, InstalledOn, InstalledBy | ConvertTo-Json
