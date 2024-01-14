$policy = net accounts
$counter = 1
$json = $policy | ForEach-Object {
    if ($_ -match ":") {
        $split = $_ -split ":", 2
        # Instead of using Key names, use a consistent index
        $value = $split[1].Trim()
        [PSCustomObject]@{Index = $counter; Value = $value}
        $counter++
    }
} | ConvertTo-Json

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$json
