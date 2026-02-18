# ⚡ INICIO RÁPIDO - CAFE.AI MARKETING SYSTEM

## 🚨 SOLUCIÓN AL ERROR: "ModuleNotFoundError: No module named 'langgraph'"

### PASO 1: Abre tu Terminal/CMD

En Windows:
- Presiona `Win + R`
- Escribe `cmd` y presiona Enter

### PASO 2: Navega a la carpeta del proyecto

```bash
cd "C:\Users\manue\OneDrive\Escritorio\MCD&IA\Ciclo 6\Desarrollo de Agentes en IA\Laboratorio 3"
```

### PASO 3: Instala las dependencias

**Opción A - Instalación Automática (RECOMENDADA):**

En Windows:
```bash
install_windows.bat
```

En Mac/Linux:
```bash
chmod +x install_mac_linux.sh
./install_mac_linux.sh
```

**Opción B - Instalación Manual:**

```bash
pip install -r requirements.txt
```

Si el comando anterior falla, prueba:
```bash
python -m pip install -r requirements.txt
```

### PASO 4: Configura tu LLM

**Opción A - OpenAI (Requiere API Key, de pago):**

1. Crea un archivo llamado `.env` en la misma carpeta
2. Agrega tu API key:
```
OPENAI_API_KEY=sk-tu-api-key-aqui
OPENAI_MODEL=gpt-4
```

**Opción B - Ollama (GRATIS, local, recomendado para empezar):**

1. Descarga Ollama: https://ollama.ai/download
2. Instala y ejecuta
3. Descarga el modelo:
```bash
ollama pull llama3.2
```
4. Edita `cafe_ai_marketing_team.py` línea 17-18:
```python
# Comenta esta línea:
# llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.7)

# Descomenta esta línea:
llm = ChatOllama(model="llama3.2:latest", temperature=0.7)
```

### PASO 5: ¡Ejecuta el sistema!

```bash
python cafe_ai_marketing_team.py
```

O prueba los ejemplos:
```bash
python cafe_ai_marketing_team.py --demo
```

---

## ✅ VERIFICACIÓN RÁPIDA

Después de instalar, verifica que todo funcione:

```bash
python -c "import langgraph; import langchain; print('TODO OK!')"
```

Si ves "TODO OK!", estás listo para usar el sistema.

---

## 📚 ARCHIVOS INCLUIDOS

1. **cafe_ai_marketing_team.py** - Código principal del sistema
2. **requirements.txt** - Lista de dependencias
3. **README_CAFE_AI.md** - Documentación completa
4. **EJEMPLOS_CAFE_AI.md** - Casos de uso y ejemplos
5. **ARQUITECTURA_VISUAL.md** - Diagramas y explicaciones
6. **INSTALACION_Y_TROUBLESHOOTING.md** - Solución de problemas (LEE ESTO SI TIENES ERRORES)
7. **install_windows.bat** - Instalador automático para Windows
8. **install_mac_linux.sh** - Instalador automático para Mac/Linux

---

## 🆘 ¿PROBLEMAS?

Consulta **INSTALACION_Y_TROUBLESHOOTING.md** - tiene soluciones para todos los errores comunes.

---

## 📊 EJEMPLO DE USO

```
📝 Describe la campaña que necesitas: 
> Crea un post de Instagram anunciando nuestra gran apertura

[El sistema genera automáticamente:]
✓ Concepto creativo
✓ Copy persuasivo
✓ Brief de diseño
✓ Campaña completa aprobada
```

---

## 🎯 TU PRIMER CAMPAÑA

1. Ejecuta: `python cafe_ai_marketing_team.py`
2. Escribe: "Crea un post de Instagram anunciando nuestra apertura"
3. ¡Espera a que los 5 agentes trabajen!
4. Recibe tu campaña completa

---

**¡Empecemos! ☕🚀**
