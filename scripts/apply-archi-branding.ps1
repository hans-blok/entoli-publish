# Doel: Entoli-merkstyling (opnieuw) toepassen op het door Archi gegenereerde model.css.
# Archi overschrijft doc/views/css/model.css volledig bij elke HTML-export van het model,
# dus dit script moet na elke export opnieuw gedraaid worden, voor je commit/publiceert.
#
# Gebruik:
#   powershell -File scripts/apply-archi-branding.ps1

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceCss = Join-Path $repoRoot "doc\branding\archi-model.css"
$targetCss = Join-Path $repoRoot "doc\views\css\model.css"

$markerStart = "/* ENTOLI-BRANDING START - zie doc/branding/archi-model.css, niet direct hier bewerken */"
$markerEnd = "/* ENTOLI-BRANDING END */"

if (-not (Test-Path $sourceCss)) {
    throw "Bronbestand niet gevonden: $sourceCss"
}
if (-not (Test-Path $targetCss)) {
    throw "Doelbestand niet gevonden: $targetCss (heb je het model al ge-exporteerd vanuit Archi?)"
}

$brandingBlock = "$markerStart`r`n" + (Get-Content $sourceCss -Raw) + "`r`n$markerEnd"

$content = Get-Content $targetCss -Raw

$pattern = [regex]::Escape($markerStart) + "[\s\S]*?" + [regex]::Escape($markerEnd)
$regex = [regex]::new($pattern)
if ($regex.IsMatch($content)) {
    $evaluator = [System.Text.RegularExpressions.MatchEvaluator] { param($m) $brandingBlock }
    $newContent = $regex.Replace($content, $evaluator)
    Set-Content -Path $targetCss -Value $newContent -Encoding utf8 -NoNewline
    Write-Host "Entoli-branding bijgewerkt in $targetCss"
} else {
    Add-Content -Path $targetCss -Value "`r`n$brandingBlock" -Encoding utf8
    Write-Host "Entoli-branding toegevoegd aan $targetCss"
}
