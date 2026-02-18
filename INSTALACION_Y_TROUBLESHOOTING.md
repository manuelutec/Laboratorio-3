# 🔧 GUÍA DE INSTALACIÓN Y SOLUCIÓN DE PROBLEMAS

## ❌ ERROR COMÚN: ModuleNotFoundError

```
ModuleNotFoundError: No module named 'langgraph'
```

**CAUSA**: Las dependencias no están instaladas en tu entorno de Python.

---

## ✅ SOLUCIÓN PASO A PASO

### Opción 1: Instalación Rápida (RECOMENDADA)

```bash
# En tu terminal/CMD, navega a la carpeta del proyecto:
cd "C:\Users\manue\OneDrive\Escritorio\MCD&IA\Ciclo 6\Desarrollo de Agentes en IA\Laboratorio 3"

# Instala todas las dependencias:
pip install -r requirements.txt
```

### Opción 2: Instalación Manual

Si la Opción 1 no funciona, instala una por una:

```bash
pip install langgraph
pip install langchain
pip install langchain-core
pip install langchain-openai
pip install langchain-ollama
pip install python-dotenv
pip install pydantic
pip install typing-extensions
```

### Opción 3: Con Entorno Virtual (MÁS LIMPIO)

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el script
python cafe_ai_marketing_team.py
```

---

## 🔍 VERIFICAR INSTALACIÓN

Después de instalar, verifica que todo esté correcto:

```bash
python -c "import langgraph; print('LangGraph OK')"
python -c "import langchain; print('LangChain OK')"
python -c "import langchain_openai; print('OpenAI OK')"
```

Si todos imprimen "OK", ¡estás listo!

---

## ⚙️ CONFIGURACIÓN ADICIONAL

### 1. Crear archivo .env

Crea un archivo llamado `.env` en la misma carpeta que `cafe_ai_marketing_team.py`:

```env
OPENAI_API_KEY=tu_api_key_aqui
OPENAI_MODEL=gpt-4
```

**¿No tienes API key de OpenAI?** No hay problema, puedes usar Ollama (ver abajo).

### 2. Opción A: Usar OpenAI (Requiere API Key)

1. Ve a https://platform.openai.com/api-keys
2. Crea una API key
3. Agrégala al archivo `.env`

**Costo aproximado:**
- GPT-4: ~$0.03 por campaña
- GPT-3.5-Turbo: ~$0.002 por campaña

### 3. Opción B: Usar Ollama (GRATIS, Local)

Si prefieres usar modelos locales y no pagar:

```bash
# 1. Descargar Ollama
# Visita: https://ollama.ai/download
# Descarga e instala para Windows

# 2. Descargar modelo
ollama pull llama3.2

# 3. En el archivo cafe_ai_marketing_team.py, línea 17-18:
# Comenta la línea de OpenAI y descomenta la de Ollama:

# llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.7)  # ← Comentar esta
llm = ChatOllama(model="llama3.2:latest", temperature=0.7)  # ← Descomentar esta
```

---

## 🚀 EJECUTAR EL SISTEMA

Una vez instalado todo:

```bash
# Modo interactivo
python cafe_ai_marketing_team.py

# Modo demo (ejemplos predefinidos)
python cafe_ai_marketing_team.py --demo
```

---

## 🐛 PROBLEMAS COMUNES Y SOLUCIONES

### Problema 1: "pip no es reconocido como comando"

**Solución:**
```bash
# Usa python -m pip en lugar de pip
python -m pip install -r requirements.txt
```

### Problema 2: "Permission denied" o "Access denied"

**Solución:**
```bash
# Instala como usuario (sin requerir admin)
pip install --user -r requirements.txt
```

### Problema 3: Versiones incompatibles

**Solución:**
```bash
# Actualiza pip primero
python -m pip install --upgrade pip

# Luego instala dependencias
pip install -r requirements.txt
```

### Problema 4: "SSL Certificate Error"

**Solución:**
```bash
# Instala confiando en el host
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Problema 5: Ya tengo LangChain pero versión antigua

**Solución:**
```bash
# Actualiza todas las dependencias
pip install --upgrade langgraph langchain langchain-openai
```

### Problema 6: Error con pydantic v1 vs v2

**Solución:**
```bash
# Asegúrate de tener pydantic v2
pip install --upgrade pydantic>=2.0.0
```

### Problema 7: Ollama no conecta

**Solución:**
```bash
# 1. Verifica que Ollama esté corriendo
ollama list

# 2. Si no está corriendo, inicia el servicio
# En Windows: busca Ollama en el menú de inicio y ábrelo

# 3. Prueba el modelo
ollama run llama3.2
```

### Problema 8: "Rate limit exceeded" con OpenAI

**Solución:**
- Espera unos minutos y reintenta
- Verifica tu plan en OpenAI (necesitas créditos)
- Usa Ollama como alternativa gratuita

### Problema 9: Respuestas muy lentas

**Posibles causas y soluciones:**

Con OpenAI:
- Es normal, GPT-4 puede tomar 10-30 segundos por agente
- Usa GPT-3.5-Turbo para respuestas más rápidas (cambia en .env)

Con Ollama:
- Primera vez es lenta (carga el modelo)
- Después es más rápido
- Usa un modelo más pequeño: `ollama pull llama3.2:1b`

### Problema 10: "Out of memory" con Ollama

**Solución:**
```bash
# Usa un modelo más pequeño
ollama pull llama3.2:1b  # Versión de 1B parámetros (más ligera)

# En el código, cambia:
llm = ChatOllama(model="llama3.2:1b", temperature=0.7)
```

---

## 📊 VERIFICACIÓN FINAL

Antes de ejecutar, verifica:

✅ Python instalado (3.10 o superior)
```bash
python --version
```

✅ Dependencias instaladas
```bash
pip list | findstr langgraph
```

✅ Archivo .env creado (si usas OpenAI)
```bash
# Debe existir en la misma carpeta
```

✅ Ollama corriendo (si usas Ollama)
```bash
ollama list
```

---

## 🎯 QUICK START (RESUMEN)

### Para usuarios con OpenAI API:
```bash
cd ruta/a/tu/proyecto
pip install -r requirements.txt
# Crea .env con tu API key
python cafe_ai_marketing_team.py
```

### Para usuarios sin API (usando Ollama):
```bash
# 1. Instala Ollama desde https://ollama.ai
# 2. Descarga modelo
ollama pull llama3.2

# 3. Instala dependencias Python
pip install -r requirements.txt

# 4. Edita cafe_ai_marketing_team.py línea 17-18
# (comenta OpenAI, descomenta Ollama)

# 5. Ejecuta
python cafe_ai_marketing_team.py
```

---

## 💬 ¿AÚN TIENES PROBLEMAS?

Si después de seguir esta guía sigues teniendo errores:

1. **Copia el error completo** que aparece en la consola
2. **Verifica** qué línea del código está fallando
3. **Revisa** que hayas seguido todos los pasos
4. **Intenta** con la opción de Ollama si OpenAI da problemas
5. **Considera** crear un entorno virtual limpio

---

## 📝 COMANDOS ÚTILES DE DIAGNÓSTICO

```bash
# Ver versión de Python
python --version

# Ver paquetes instalados
pip list

# Ver info de un paquete específico
pip show langgraph

# Ver dónde está instalado Python
python -c "import sys; print(sys.executable)"

# Ver dónde busca módulos
python -c "import sys; print('\n'.join(sys.path))"

# Probar import de módulos críticos
python -c "import langgraph, langchain, pydantic; print('All OK!')"
```

---

## 🎓 NOTAS ADICIONALES

### Diferencia entre pip y conda

Si usas Anaconda/Miniconda:
```bash
# Crea entorno conda
conda create -n cafeai python=3.11
conda activate cafeai

# Instala con pip dentro del entorno
pip install -r requirements.txt
```

### Para sistemas con múltiples versiones de Python

```bash
# Usa python3 y pip3 explícitamente
python3 --version
pip3 install -r requirements.txt
python3 cafe_ai_marketing_team.py
```

---

**🎉 Una vez que todo funcione, deberías ver:**

```
☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕
                                   CAFE.AI
                    Sistema de Marketing Multiagente
☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕

================================================================================
 🚀 SISTEMA DE MARKETING CAFE.AI - EQUIPO PUBLICITARIO 🚀 
================================================================================

Equipo disponible:
  🎯 Router - Clasifica tipo de contenido
  🎨 Creative - Genera conceptos creativos
  ✍️  Copywriter - Escribe textos persuasivos
  🖼️  Designer - Crea briefs de diseño
  👔 Supervisor - Revisa y aprueba campaña final

================================================================================

📝 Describe la campaña que necesitas (o 'exit' para salir):
```

**¡Y listo! Sistema funcionando correctamente. ☕🚀**
