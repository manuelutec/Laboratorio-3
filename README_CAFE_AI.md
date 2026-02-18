# 🚀 Sistema Multiagente de Marketing para Cafe.AI ☕🤖

## 📋 Descripción del Proyecto

Sistema inteligente de creación de campañas publicitarias para **Cafe.AI** utilizando arquitectura multiagente con LangGraph. El sistema coordina un equipo completo de especialistas en marketing que trabajan colaborativamente para crear campañas de alto impacto para redes sociales.

---

## 🏗️ Arquitectura del Sistema

### Tipo: **Routing + Pipeline Secuencial**

```
┌─────────────────────────────────────────────────────────┐
│                    FLUJO DEL SISTEMA                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  USER INPUT   │
                    │  (Brief)      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  ROUTER 🎯    │
                    │  Clasifica    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  CREATIVE 🎨  │
                    │  Concepto     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ COPYWRITER ✍️ │
                    │  Copy         │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  DESIGNER 🖼️  │
                    │  Brief        │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ SUPERVISOR 👔 │
                    │  Aprobación   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ FINAL OUTPUT  │
                    │  Campaña ✨   │
                    └───────────────┘
```

---

## 👥 El Equipo de Agentes

### 1. 🎯 **Router Agent (Enrutador)**
- **Rol**: Estratega de marketing digital
- **Función**: Clasifica el tipo de contenido y estilo creativo
- **Output**: 
  - Tipo de contenido (Instagram, Twitter, Facebook, etc.)
  - Estilo creativo (minimalista, vibrante, profesional, etc.)
  - Prioridad (alta, media, baja)

### 2. 🎨 **Creative Agent (Director Creativo)**
- **Rol**: Generador de conceptos creativos
- **Función**: Crea la gran idea y concepto visual
- **Output**:
  - Concepto principal de la campaña
  - Elementos visuales clave
  - Mood y atmósfera
  - Hooks creativos
  - Referencias de inspiración

### 3. ✍️ **Copywriter Agent (Redactor)**
- **Rol**: Especialista en textos persuasivos
- **Función**: Convierte el concepto en copy efectivo
- **Output**:
  - Headlines impactantes
  - Copy adaptado a la plataforma
  - Call-to-action claro
  - Hashtags relevantes
  - Tono de voz alineado a marca

### 4. 🖼️ **Designer Agent (Diseñador)**
- **Rol**: Diseñador gráfico líder
- **Función**: Crea brief de diseño ejecutable
- **Output**:
  - Especificaciones técnicas
  - Paleta de colores (HEX codes)
  - Tipografía sugerida
  - Layout y composición
  - Mood board y referencias

### 5. 👔 **Supervisor Agent (Director de Marketing)**
- **Rol**: Coordinador y revisor final
- **Función**: Integra todos los elementos y aprueba
- **Output**:
  - Resumen ejecutivo
  - Estrategia consolidada
  - KPIs esperados
  - Plan de ejecución
  - Aprobación final

---

## 🎯 Sobre Cafe.AI

### Propuesta de Valor
Café donde la tecnología y el sabor convergen. Un espacio diseñado para:
- 💻 Innovadores y desarrolladores
- 🚀 Profesionales tech y creativos
- ☕ Amantes del café excepcional
- 🌐 Comunidad tech local

### Diferenciadores
- ⚡ WiFi ultra rápido
- 🎨 Ambiente diseñado para productividad
- 🤝 Espacio de networking tech
- 📊 "Café + IA = Tu nuevo espacio de trabajo"

### Tono de Marca
- Innovador pero accesible
- Profesional pero amigable
- Tech-savvy pero humano
- Inspirador y energético

---

## 🛠️ Instalación

### Requisitos Previos
```bash
Python 3.10+
OpenAI API Key o Ollama instalado
```

### Instalación de Dependencias
```bash
pip install langgraph langchain-openai langchain-ollama python-dotenv pydantic
```

### Configuración
1. Crea un archivo `.env` en la raíz del proyecto:
```env
OPENAI_API_KEY=tu_api_key_aqui
OPENAI_MODEL=gpt-4
```

2. O configura para usar Ollama (opción local):
```python
# En el archivo, descomenta:
llm = ChatOllama(model="llama3.2:latest", temperature=0.7)
```

---

## 🚀 Uso

### Modo Interactivo
```bash
python cafe_ai_marketing_team.py
```

Ejemplos de solicitudes:
```
📝 Describe la campaña que necesitas:
> Crea un post para Instagram anunciando nuestra apertura

📝 Describe la campaña que necesitas:
> Necesito un thread de Twitter sobre por qué Cafe.AI es diferente

📝 Describe la campaña que necesitas:
> Diseña un anuncio de Facebook para atraer desarrolladores
```

### Modo Demo
```bash
python cafe_ai_marketing_team.py --demo
```

Ejecuta 3 ejemplos predefinidos automáticamente.

---

## 📊 Tipos de Contenido Soportados

| Plataforma | Tipo | Especificaciones |
|------------|------|------------------|
| 📸 Instagram | Post | 1080x1080px o 1080x1350px |
| 📱 Instagram | Story | 1080x1920px (9:16) |
| 🐦 Twitter/X | Thread | 1200x675px por imagen |
| 📘 Facebook | Ad | 1200x628px |
| 💼 LinkedIn | Post | 1200x627px |
| 🎥 Video | Script | 1080x1920px o 1920x1080px |

---

## 💾 Funcionalidades

### ✅ Generación Automática
- Concepto creativo completo
- Copy persuasivo adaptado
- Brief de diseño detallado
- Campaña integrada y aprobada

### 💾 Exportación
- Guarda campañas en archivos `.txt`
- Timestamp automático
- Todas las secciones incluidas

### 🎨 Personalización
- Adapta tono según plataforma
- Estilos visuales variables
- Priorización inteligente

---

## 🔧 Estructura del Código

### State Management
```python
class MarketingState(TypedDict):
    messages: list  # Historial de conversación
    content_type: str  # Tipo de contenido
    creative_style: str  # Estilo visual
    priority: str  # Prioridad
    creative_concept: str  # Output creativo
    copy_text: str  # Output copywriter
    design_brief: str  # Output diseñador
    final_campaign: str  # Output supervisor
```

### Flujo de LangGraph
```python
graph_builder.add_edge(START, "router")
graph_builder.add_conditional_edges("router", route_to_creative)
graph_builder.add_conditional_edges("creative", route_to_copywriter)
graph_builder.add_conditional_edges("copywriter", route_to_designer)
graph_builder.add_conditional_edges("designer", route_to_supervisor)
graph_builder.add_edge("supervisor", END)
```

---

## 🎓 Conceptos Aplicados

1. **Routing**: Clasificación inteligente de tipo de contenido
2. **Prompt Chaining**: Flujo secuencial de agentes
3. **State Management**: Estado compartido entre agentes
4. **Structured Output**: Clasificación tipada con Pydantic
5. **Conditional Edges**: Routing dinámico en LangGraph

### Arquitectura Multiagente
- ✅ **Especialización**: Cada agente es experto en su dominio
- ✅ **Pipeline**: Flujo secuencial optimizado
- ✅ **Supervisión**: Agente supervisor final
- ✅ **Escalabilidad**: Fácil agregar nuevos agentes
- ✅ **Modularidad**: Cada agente es independiente

---

### 🎨 Variaciones de Arquitectura
- **Paralelización**: Ejecutar Creative + Copywriter simultáneamente
- **Evaluator-Optimizer**: Ciclo de refinamiento iterativo
- **Swarm**: Transferencias peer-to-peer entre agentes

---

## 🐛 Troubleshooting

### Error: API Key no encontrada
```bash
# Verifica tu archivo .env
export OPENAI_API_KEY=tu_key_aqui
```

### Error: Modelo no disponible
```python
# Cambia a Ollama si no tienes API de OpenAI
llm = ChatOllama(model="llama3.2:latest", temperature=0.7)
```

### Error: Timeout
```python
# Aumenta temperatura o reduce complejidad del prompt
llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.7, timeout=60)
```

---

## 📝 Ejemplos de Output

### Ejemplo 1: Post de Instagram
```
📸 TIPO: Instagram Post
🎨 ESTILO: Vibrante
⭐ PRIORIDAD: Alta

CONCEPTO CREATIVO:
"El Futuro del Café es Ahora"
[Concepto completo con elementos visuales...]

COPY:
☕ Donde el código se encuentra con la cafeína 💻

[Copy persuasivo completo...]

#CafeAI #TechCafe #CodeAndCoffee

DESIGN BRIEF:
- Dimensiones: 1080x1080px
- Paleta: #3E2723 (café) + #00E676 (tech green)
[Brief completo...]
```

