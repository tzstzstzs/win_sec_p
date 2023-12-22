# get_active_ports.ps1
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State | ConvertTo-Json
