#!/bin/bash
# Script de instalacion automatica para Cafe.AI Marketing System
# Mac/Linux Bash Script

echo "========================================"
echo "   CAFE.AI - INSTALACION AUTOMATICA"
echo "========================================"
echo ""

echo "[1/5] Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no esta instalado"
    echo "Por favor instala Python 3.10 o superior"
    exit 1
fi
python3 --version
echo "✓ Python encontrado"
echo ""

echo "[2/5] Actualizando pip..."
python3 -m pip install --upgrade pip
echo ""

echo "[3/5] Instalando dependencias..."
echo "Esto puede tomar algunos minutos..."
if pip3 install -r requirements.txt; then
    echo "✓ Dependencias instaladas"
else
    echo ""
    echo "ERROR: Fallo en la instalacion"
    echo "Intentando instalacion alternativa..."
    pip3 install --user -r requirements.txt
fi
echo ""

echo "[4/5] Verificando instalacion..."
python3 -c "import langgraph; print('✓ LangGraph instalado')"
python3 -c "import langchain; print('✓ LangChain instalado')"
python3 -c "import pydantic; print('✓ Pydantic instalado')"
echo ""

echo "[5/5] Configuracion..."
if [ ! -f .env ]; then
    echo "Creando archivo .env..."
    cat > .env << EOF
# Configuracion de Cafe.AI Marketing System
# Opcion 1: Usar OpenAI
OPENAI_API_KEY=tu_api_key_aqui
OPENAI_MODEL=gpt-4

# Opcion 2: Si usas Ollama, edita cafe_ai_marketing_team.py
# y comenta la linea de OpenAI, descomenta la de Ollama
EOF
    echo "✓ Archivo .env creado"
    echo "  IMPORTANTE: Edita .env y agrega tu API key de OpenAI"
    echo "  O configura Ollama siguiendo el README"
else
    echo "✓ Archivo .env ya existe"
fi
echo ""

echo "========================================"
echo "   INSTALACION COMPLETADA"
echo "========================================"
echo ""
echo "Proximos pasos:"
echo "1. Edita el archivo .env con tu API key de OpenAI"
echo "   O configura Ollama para uso local gratuito"
echo ""
echo "2. Ejecuta el sistema:"
echo "   python3 cafe_ai_marketing_team.py"
echo ""
echo "3. O prueba los demos:"
echo "   python3 cafe_ai_marketing_team.py --demo"
echo ""
echo "Para mas ayuda, consulta INSTALACION_Y_TROUBLESHOOTING.md"
echo ""
