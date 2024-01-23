# get_active_ports.ps1
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State | ConvertTo-Json
