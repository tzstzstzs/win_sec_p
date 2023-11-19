# get_users.ps1
# Get-LocalUser | Select-Object Name, Description, Enabled, LastLogon | ConvertTo-Json

$users = Get-LocalUser | Where-Object { $_.Enabled -eq $true } | Select-Object Name, Description, Enabled, LastLogon
    $data = @()
    foreach ($user in $users) {
        $groups = Get-LocalGroup | Where-Object { $_.Members -match $user.Name }
        $groupNames = $groups | Select-Object -ExpandProperty Name
        $obj = [PSCustomObject]@{
            Username = $user.Name
            Description = $user.Description
            Enabled = $user.Enabled
            LastLogon = $user.LastLogon
            Groups = $groupNames -join ', '
        }
        $data += $obj
    }
    $data | ConvertTo-Json