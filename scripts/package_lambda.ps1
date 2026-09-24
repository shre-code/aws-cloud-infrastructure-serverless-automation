$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$build = Join-Path $root "build/lambda"
$zip = Join-Path $root "build/lambda.zip"

Remove-Item $build -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item $zip -Force -ErrorAction SilentlyContinue

New-Item -ItemType Directory -Path $build -Force | Out-Null
Copy-Item "$root/lambda/handler.py" $build
Copy-Item "$root/lambda/requirements.txt" $build

Compress-Archive -Path "$build/*" -DestinationPath $zip

Write-Host "Created $zip"
