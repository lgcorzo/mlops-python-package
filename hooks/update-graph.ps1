# .git/hooks/update-graph.ps1
# Script de PowerShell para actualizar la wiki de Graphify en Windows.
# Se ejecuta en segundo plano con ventana oculta.

# 1. Guardia de Procesos: Evitar superposiciones si el usuario realiza commits rápidos
$graphifyProcess = Get-Process -Name "graphify" -ErrorAction SilentlyContinue

if ($graphifyProcess) {
    exit 0
}

# Función para iniciar procesos de forma silenciosa y en segundo plano
function Start-BgProcess {
    param (
        [string]$FileName,
        [string]$Arguments
    )
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $FileName
    $psi.Arguments = $Arguments
    $psi.WindowStyle = [System.Diagnostics.ProcessWindowStyle]::Hidden
    $psi.CreateNoWindow = $true
    $psi.UseShellExecute = $false
    try {
        [System.Diagnostics.Process]::Start($psi) | Out-Null
    } catch {
        # Omitir errores de inicio silencioso
    }
}

# 2. Lanzar actualización de Graphify
$graphifyGlobal = Get-Command graphify -ErrorAction SilentlyContinue
if ($graphifyGlobal) {
    Start-BgProcess -FileName "graphify" -Arguments "update ."
} else {
    $uvCheck = Get-Command uv -ErrorAction SilentlyContinue
    if ($uvCheck) {
        Start-BgProcess -FileName "uvx" -Arguments "--from graphifyy graphify update ."
    }
}
