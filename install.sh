#!/bin/bash
# install.sh
# Script de instalación y configuración automatizada para Ubuntu / Linux.
# Configura Ollama, uv, code-review-graph, graphify y Git Hooks.

# Colores para salida
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # Sin color

echo -e "${CYAN}=== Iniciando Instalación del Ecosistema DeepWiki Documenter (Ubuntu/Linux) ===${NC}"

# 1. Verificar/Instalar 'uv' (herramienta de empaquetado de Python)
echo -e "${YELLOW}Verificando instalación de uv...${NC}"
if ! command -v uv &> /dev/null; then
    echo -e "${CYAN}uv no detectado. Instalando uv automáticamente...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Cargar uv en la sesión actual
    source $HOME/.local/bin/env
else
    echo -e "${GREEN}¡uv ya está instalado!${NC}"
fi

# 2. Instalar herramientas globales de Python utilizando uv
echo -e "${YELLOW}Instalando graphify...${NC}"
# Graphify package naming may vary across releases/channels.
if ! uv tool install graphify; then
    echo -e "${YELLOW}No se pudo instalar 'graphify'. Intentando con 'graphifyy'...${NC}"
    uv tool install graphifyy
fi

# Asegurar que el PATH del usuario incluya el directorio de herramientas de uv
export PATH="$HOME/.local/bin:$PATH"

# 3. Verificar archivos de configuración esperados
echo -e "${YELLOW}Verificando archivos ignore en la raíz del repositorio...${NC}"
[ ! -f "./.graphifyignore" ] && echo -e "${YELLOW}ADVERTENCIA: Falta el archivo .graphifyignore en la raíz del repositorio.${NC}"

# 4. Instalar Git Hooks locales
if [ -d ".git" ]; then
    echo -e "${YELLOW}Instalando Git Hooks para automatizar la wiki...${NC}"
    HOOKS_DIR=".git/hooks"
    mkdir -p "$HOOKS_DIR"
    cp "./hooks/post-commit" "./$HOOKS_DIR/post-commit"
    cp "./hooks/post-checkout" "./$HOOKS_DIR/post-checkout"
    cp "./hooks/update-graph.ps1" "./$HOOKS_DIR/update-graph.ps1"
    cp "./hooks/update-graph-checkout.ps1" "./$HOOKS_DIR/update-graph-checkout.ps1"
    
    # Otorgar permisos de ejecución a los hooks
    chmod +x "./$HOOKS_DIR/post-commit"
    chmod +x "./$HOOKS_DIR/post-checkout"
    echo -e "${GREEN}¡Git Hooks instalados y con permisos de ejecución!${NC}"
else
    echo -e "${YELLOW}ADVERTENCIA: No se detectó un directorio '.git'. Asegúrate de estar en la raíz de un repositorio Git para instalar los hooks.${NC}"
fi

# 5. Sincronizando skills de Graphify para evitar desfases de versión...
echo -e "${CYAN}Sincronizando skills de Graphify para evitar desfases de versión...${NC}"
graphify install --platform copilot

echo -e "${CYAN}Actualizando la DeepWiki (graphify)...${NC}"
graphify update .

echo -e "${CYAN}Regenerando comunidades del reporte de Graphify...${NC}"
graphify cluster-only .

echo -e "${GREEN}=== ¡Instalación Completada con Éxito! ===${NC}"
echo -e "${GREEN}GitHub Copilot ahora cuenta con búsquedas semánticas locales y mantiene tu DeepWiki viva.${NC}"
echo -e "${CYAN}Nota: Por favor, ejecuta 'source $HOME/.bashrc' (o tu archivo de configuración de shell) para aplicar los cambios de variables.${NC}"
