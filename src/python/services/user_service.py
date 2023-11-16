# src/python/services/user_service.py
import subprocess
import json


def get_windows_users_with_powershell():
    # PowerShell command to get users and their group memberships
    command = """
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
    """
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception("Failed to retrieve users with PowerShell: " + result.stderr)

    # Parse JSON output from PowerShell
    users_data = json.loads(result.stdout)
    return users_data
