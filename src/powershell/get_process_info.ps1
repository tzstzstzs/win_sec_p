$processInfo = Get-Process
$combinedInfo = foreach ($p in $processInfo) {
    # Get the WMI object for the specific process
    $wmiCurrentProcess = Get-WmiObject Win32_Process -Filter "ProcessId = $($p.Id)"

    # Initialize variables
    $userName = "Not Available"
    $parentId = $null
    $executablePath = $null

    if ($wmiCurrentProcess -ne $null) {
        # Get owner of the process
        try {
            $owner = $wmiCurrentProcess.GetOwner()
            $userName = "$($owner.Domain)\$($owner.User)"
        } catch {
            $userName = "Access Denied"
        }
        $parentId = $wmiCurrentProcess.ParentProcessId
        $executablePath = $wmiCurrentProcess.ExecutablePath
    }

    [PSCustomObject]@{
        ProcessName = $p.ProcessName
        Id = $p.Id
        CPU = $p.CPU
        WorkingSet = $p.WorkingSet
        ParentId = $parentId
        ExecutablePath = $executablePath
        AssociatedUser = $userName
        # NetworkActivity and OpenFileHandles would need to be added here
    }
}

# Convert to JSON
$json = $combinedInfo | ConvertTo-Json -Depth 5
$json
