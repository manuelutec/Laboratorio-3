@echo off
REM Script de instalacion automatica para Cafe.AI Marketing System
REM Windows Batch Script

echo ========================================
echo    CAFE.AI - INSTALACION AUTOMATICA
echo ========================================
echo.

echo [1/5] Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Por favor instala Python 3.10 o superior desde https://www.python.org
    pause
    exit /b 1
)
echo OK: Python encontrado
echo.

echo [2/5] Actualizando pip...
python -m pip install --upgrade pip
echo.

echo [3/5] Instalando dependencias...
echo Esto puede tomar algunos minutos...
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Fallo en la instalacion
    echo Intentando instalacion alternativa...
    pip install --user -r requirements.txt
)
echo.

echo [4/5] Verificando instalacion...
python -c "import langgraph; print('✓ LangGraph instalado')"
python -c "import langchain; print('✓ LangChain instalado')"
python -c "import pydantic; print('✓ Pydantic instalado')"
echo.

echo [5/5] Configuracion...
if not exist .env (
    echo Creando archivo .env...
    (
        echo # Configuracion de Cafe.AI Marketing System
        echo # Opcion 1: Usar OpenAI
        echo OPENAI_API_KEY=tu_api_key_aqui
        echo OPENAI_MODEL=gpt-4
        echo.
        echo # Opcion 2: Si usas Ollama, edita cafe_ai_marketing_team.py
        echo # y comenta la linea de OpenAI, descomenta la de Ollama
    ) > .env
    echo ✓ Archivo .env creado
    echo   IMPORTANTE: Edita .env y agrega tu API key de OpenAI
    echo   O configura Ollama siguiendo el README
) else (
    echo ✓ Archivo .env ya existe
)
echo.

echo ========================================
echo    INSTALACION COMPLETADA
echo ========================================
echo.
echo Proximos pasos:
echo 1. Edita el archivo .env con tu API key de OpenAI
echo    O configura Ollama para uso local gratuito
echo.
echo 2. Ejecuta el sistema:
echo    python cafe_ai_marketing_team.py
echo.
echo 3. O prueba los demos:
echo    python cafe_ai_marketing_team.py --demo
echo.
echo Para mas ayuda, consulta INSTALACION_Y_TROUBLESHOOTING.md
echo.
pause
