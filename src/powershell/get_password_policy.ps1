# get_password_policy.ps1

$policy = net accounts
$counter = 1
$json = $policy | ForEach-Object {
    if ($_ -match ":") {
        $split = $_ -split ":", 2
        $key = $split[0].Trim()
        $value = $split[1].Trim()
        [PSCustomObject]@{Line = $counter; Key = $key; Value = $value}
        $counter++
    }
} | ConvertTo-Json

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$json
