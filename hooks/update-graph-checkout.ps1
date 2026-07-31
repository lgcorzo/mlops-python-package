# .git/hooks/update-graph-checkout.ps1
# Script de PowerShell para reconstruir o actualizar el grafo en Windows tras cambiar de rama.
# Recibe argumentos: $args[0] = commit_anterior, $args[1] = commit_nuevo, $args[2] = is_branch_checkout (1 o 0)

# Validar que sea un checkout de rama real
if ($args.Count -lt 3 -or $args[2] -ne "1") {
    exit 0
}

# 1. Guardia de Procesos
$graphifyProcess = Get-Process -Name "graphify" -ErrorAction SilentlyContinue

if ($graphifyProcess) {
    exit 0
}

# Función para iniciar procesos de forma silenciosa
function Start-BgProcess {
    param (
        [string]$FileName,
        [string]$Arguments,
        [hashtable]$EnvVars = $null
    )
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $FileName
    $psi.Arguments = $Arguments
    $psi.WindowStyle = [System.Diagnostics.ProcessWindowStyle]::Hidden
    $psi.CreateNoWindow = $true
    $psi.UseShellExecute = $false
    if ($EnvVars) {
        foreach ($key in $EnvVars.Keys) {
            $psi.EnvironmentVariables[$key] = $EnvVars[$key]
        }
    }
    try {
        [System.Diagnostics.Process]::Start($psi) | Out-Null
    } catch {
        # Omitir errores
    }
}

# 2. Contar archivos modificados
$changedFilesCount = 0
try {
    $diff = git diff --name-only $args[0] $args[1]
    $changedFilesCount = ($diff | Measure-Object).Count
} catch {
    $changedFilesCount = 0
}

$graphifyGlobal = Get-Command graphify -ErrorAction SilentlyContinue
$uvCheck = Get-Command uv -ErrorAction SilentlyContinue

if ($changedFilesCount -gt 5) {
    # --- CAMBIO GRANDE: Reconstrucción Completa (build) ---
    if ($graphifyGlobal) {
        $envMap = @{ "GRAPHIFY_FORCE" = "true" }
        Start-BgProcess -FileName "graphify" -Arguments "update ." -EnvVars $envMap
    } elseif ($uvCheck) {
        $envMap = @{ "GRAPHIFY_FORCE" = "true" }
        Start-BgProcess -FileName "uvx" -Arguments "--from graphifyy graphify update ." -EnvVars $envMap
    }
} else {
    # --- CAMBIO PEQUEÑO: Actualización Incremental (update) ---
    if ($graphifyGlobal) {
        Start-BgProcess -FileName "graphify" -Arguments "update ."
    } elseif ($uvCheck) {
        Start-BgProcess -FileName "uvx" -Arguments "--from graphifyy graphify update ."
    }
}
