from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
import os
import sys
from datetime import datetime

# Configurar encoding UTF-8 para Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
load_dotenv()

# Configuración del LLM
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
# Descomenta la línea que prefieras usar
llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.7)  # Más creatividad para marketing
# llm = ChatOllama(model="llama3.2:latest", temperature=0.7)

########################################## CONTEXTO CAFE.AI #####################################################

CAFE_AI_CONTEXT = """
CONTEXTO DE CAFE.AI =[AI]:

Café donde la tecnología y el sabor convergen, tu espacio para conectar, crear e innovar, 
una taza a la vez. Diseñado como un café inteligente para mentes creativas, con conexión 
rápida, café excepcional y un ambiente pensado para que tus mejores ideas florezcan.

PÚBLICO OBJETIVO:
- Innovadores, desarrolladores y soñadores
- Profesionales tech y creativos
- Personas que buscan espacios de cowork con buen café
- Comunidad tech local

PROPUESTA DE VALOR:
- Café excepcional + Tecnología
- WiFi ultra rápido
- Ambiente diseñado para productividad
- Espacio de networking tech
- "Café + IA = Tu nuevo espacio de trabajo"

TONO DE MARCA:
- Innovador pero accesible
- Profesional pero amigable
- Tech-savvy pero humano
- Inspirador y energético
"""

########################################## CLASIFICADOR DE CONTENIDO #####################################################

class ContentClassifier(BaseModel):
    """Clasificador de tipo de contenido a crear"""
    content_type: Literal["instagram_post", "twitter_thread", "facebook_ad", "linkedin_post", "story", "video_script"] = Field(
        description="Tipo de contenido a crear según la solicitud del usuario"
    )
    creative_style: Literal["minimalista", "vibrante", "profesional", "casual", "inspirador"] = Field(
        description="Estilo visual/creativo sugerido para el contenido"
    )
    priority: Literal["alta", "media", "baja"] = Field(
        description="Prioridad del contenido basada en urgencia o importancia"
    )

########################################## STATE DEFINITION #####################################################

class MarketingState(TypedDict):
    """Estado del sistema de marketing"""
    messages: Annotated[list, add_messages]
    content_type: str | None
    creative_style: str | None
    priority: str | None
    creative_concept: str | None  # Output del agente creativo
    copy_text: str | None  # Output del agente redactor
    design_brief: str | None  # Output del agente diseñador
    final_campaign: str | None  # Output del supervisor
    route_to: str | None  # Para routing condicional

########################################## AGENTE 1: ROUTER #####################################################

def router_agent(state: MarketingState):
    """
    Agente Router: Clasifica el tipo de contenido solicitado
    Similar al classifier en maslc.py pero para tipos de contenido
    """
    last_message = state["messages"][-1]
    
    classifier_llm = llm.with_structured_output(ContentClassifier)
    
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": f"""Eres un estratega de marketing digital para Cafe.AI.
            
{CAFE_AI_CONTEXT}

Analiza la solicitud del usuario y clasifica:
1. content_type: ¿Qué tipo de contenido quieren crear?
2. creative_style: ¿Qué estilo visual sería más efectivo?
3. priority: ¿Qué tan urgente/importante es este contenido?

Considera las mejores prácticas de cada plataforma."""
        },
        {"role": "user", "content": last_message.content}
    ])
    
    print(f"\n{'='*60}")
    print(f"[ROUTER AGENT] [ROUTER]")
    print(f"Tipo de contenido: {result.content_type}")
    print(f"Estilo creativo: {result.creative_style}")
    print(f"Prioridad: {result.priority}")
    print(f"{'='*60}\n")
    
    return {
        "content_type": result.content_type,
        "creative_style": result.creative_style,
        "priority": result.priority
    }

########################################## AGENTE 2: CREATIVO #####################################################

def creative_agent(state: MarketingState):
    """
    Agente Creativo: Genera conceptos creativos e ideas visuales
    Similar al therapist_agent pero enfocado en creatividad
    """
    last_message = state["messages"][-1]
    content_type = state.get("content_type", "instagram_post")
    creative_style = state.get("creative_style", "vibrante")
    
    messages = [
        {
            "role": "system",
            "content": f"""Eres el DIRECTOR CREATIVO del equipo de marketing de Cafe.AI.

{CAFE_AI_CONTEXT}

Tu trabajo es generar CONCEPTOS CREATIVOS innovadores y memorables.

TIPO DE CONTENIDO: {content_type}
ESTILO VISUAL: {creative_style}

Debes proporcionar:
1. **Concepto Principal**: La gran idea detrás de la campaña
2. **Elementos Visuales Clave**: Qué se debe mostrar
3. **Mood/Atmósfera**: Qué debe sentir la audiencia
4. **Hooks Creativos**: Elementos que capturan atención
5. **Referencias**: Inspiración o ejemplos del estilo

Sé innovador pero mantén la esencia de Cafe.AI: donde tech y café se encuentran."""
        },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    
    reply = llm.invoke(messages)
    
    print(f"\n{'='*60}")
    print(f"[CREATIVE AGENT] [CREATIVE]")
    print(f"Concepto generado:")
    print(f"{reply.content[:200]}...")
    print(f"{'='*60}\n")
    
    return {
        "creative_concept": reply.content,
        "messages": [{"role": "assistant", "content": f"[CREATIVO] {reply.content}"}]
    }

########################################## AGENTE 3: REDACTOR (COPYWRITER) #####################################################

def copywriter_agent(state: MarketingState):
    """
    Agente Redactor: Crea textos persuasivos y engaging
    Toma el concepto creativo y lo convierte en copy efectivo
    """
    creative_concept = state.get("creative_concept", "")
    content_type = state.get("content_type", "instagram_post")
    creative_style = state.get("creative_style", "vibrante")
    
    messages = [
        {
            "role": "system",
            "content": f"""Eres el COPYWRITER SENIOR del equipo de marketing de Cafe.AI.

{CAFE_AI_CONTEXT}

CONCEPTO CREATIVO RECIBIDO:
{creative_concept}

TIPO DE CONTENIDO: {content_type}
ESTILO: {creative_style}

Tu trabajo es crear COPY PERSUASIVO y ENGAGING:

Para Instagram/Facebook:
- Headline impactante (hook)
- Copy corto pero memorable (50-100 palabras)
- Call-to-action claro
- 3-5 hashtags relevantes
- Emojis estratégicos

Para Twitter/X:
- Thread de 3-5 tweets
- Primer tweet debe ser gancho
- Información valiosa en siguientes tweets
- CTA en último tweet

Para LinkedIn:
- Tono más profesional
- Historia o insight valioso
- 150-200 palabras
- CTA orientado a networking/visita

Para Stories:
- Textos cortos y directos
- 1-2 frases por slide
- Lenguaje conversacional
- CTAs interactivos (encuestas, preguntas, etc)

REGLAS:
✓ Mantén el tono de marca: innovador, accesible, inspirador
✓ Resalta la propuesta de valor: Café + Tech
✓ Incluye call-to-action
✓ Usa emociones y beneficios, no solo características
✓ Sé auténtico, evita clichés de marketing"""
        },
        {
            "role": "user",
            "content": f"Crea el copy para {content_type} basado en el concepto creativo proporcionado."
        }
    ]
    
    reply = llm.invoke(messages)
    
    print(f"\n{'='*60}")
    print(f"[COPYWRITER AGENT] [COPYWRITER]")
    print(f"Copy generado:")
    print(f"{reply.content[:200]}...")
    print(f"{'='*60}\n")
    
    return {
        "copy_text": reply.content,
        "messages": [{"role": "assistant", "content": f"[REDACTOR] {reply.content}"}]
    }

########################################## HELPER FUNCTIONS #####################################################

def _get_platform_specs(content_type):
    """Helper para especificaciones de cada plataforma"""
    specs = {
        "instagram_post": "1080x1080px (cuadrado) o 1080x1350px (vertical), formato JPG/PNG",
        "instagram_story": "1080x1920px (9:16), formato JPG/PNG/MP4",
        "twitter_thread": "1200x675px por imagen, formato JPG/PNG",
        "facebook_ad": "1200x628px, formato JPG/PNG",
        "linkedin_post": "1200x627px, formato JPG/PNG",
        "video_script": "1080x1920px (vertical) o 1920x1080px (horizontal), MP4"
    }
    return specs.get(content_type, "Dimensiones estándar según plataforma")

########################################## AGENTE 4: DISEÑADOR #####################################################

def designer_agent(state: MarketingState):
    """
    Agente Diseñador: Crea briefs de diseño detallados
    Proporciona especificaciones técnicas y visuales
    """
    creative_concept = state.get("creative_concept", "")
    copy_text = state.get("copy_text", "")
    content_type = state.get("content_type", "instagram_post")
    creative_style = state.get("creative_style", "vibrante")
    
    messages = [
        {
            "role": "system",
            "content": f"""Eres el DISEÑADOR GRÁFICO LÍDER del equipo de marketing de Cafe.AI.

{CAFE_AI_CONTEXT}

CONCEPTO CREATIVO:
{creative_concept}

COPY:
{copy_text}

TIPO DE CONTENIDO: {content_type}
ESTILO: {creative_style}

Tu trabajo es crear un DESIGN BRIEF detallado que un diseñador pueda ejecutar:

ESPECIFICACIONES TÉCNICAS:
- Dimensiones exactas según plataforma
- Formato de archivo (JPG, PNG, MP4, etc)
- Resolución recomendada

PALETA DE COLORES:
- Colores principales (códigos HEX)
- Sugerencia: Usar tonos cálidos de café (marrón, crema) + azul tech o verde neón
- Contraste y legibilidad

TIPOGRAFÍA:
- Fuentes sugeridas (modernas, tech-friendly pero legibles)
- Tamaños de texto
- Jerarquía visual

ELEMENTOS VISUALES:
- Imágenes/fotos necesarias (descripciones detalladas)
- Iconos o gráficos
- Composición y layout
- Espacios en blanco

MOOD BOARD:
- Referencias visuales
- Estilo fotográfico
- Tratamiento de imagen (filtros, efectos)

GUÍA DE MARCA CAFE.AI:
- Logo placement
- Consistencia con identidad de marca
- Elementos distintivos (taza de café + elementos tech)

Para {content_type}:
{_get_platform_specs(content_type)}"""
        },
        {
            "role": "user",
            "content": f"Crea el design brief completo para {content_type}"
        }
    ]
    
    reply = llm.invoke(messages)
    
    print(f"\n{'='*60}")
    print(f"[DESIGNER AGENT] [CREATIVE]")
    print(f"Design brief generado:")
    print(f"{reply.content[:200]}...")
    print(f"{'='*60}\n")
    
    return {
        "design_brief": reply.content,
        "messages": [{"role": "assistant", "content": f"[DISEÑADOR] {reply.content}"}]
    }

########################################## AGENTE 5: SUPERVISOR #####################################################

def supervisor_agent(state: MarketingState):
    """
    Agente Supervisor: Revisa, integra y aprueba la campaña final
    Similar al orquestador, coordina todos los outputs
    """
    creative_concept = state.get("creative_concept", "")
    copy_text = state.get("copy_text", "")
    design_brief = state.get("design_brief", "")
    content_type = state.get("content_type", "")
    
    messages = [
        {
            "role": "system",
            "content": f"""Eres el DIRECTOR DE MARKETING de Cafe.AI y supervisor del equipo creativo.

{CAFE_AI_CONTEXT}

Has recibido los siguientes entregables de tu equipo:

═══════════════════════════════════════
CONCEPTO CREATIVO (Creative Agent):
{creative_concept}

═══════════════════════════════════════
COPY (Copywriter Agent):
{copy_text}

═══════════════════════════════════════
DESIGN BRIEF (Designer Agent):
{design_brief}

═══════════════════════════════════════

Tu trabajo es:

1. **REVISAR**: Verificar coherencia entre concepto, copy y diseño
2. **INTEGRAR**: Asegurar que todos los elementos trabajan juntos
3. **OPTIMIZAR**: Sugerir mejoras si es necesario
4. **APROBAR**: Dar el visto bueno final con un brief ejecutivo

Proporciona un DOCUMENTO FINAL DE CAMPAÑA que incluya:

[RESUME] **RESUMEN EJECUTIVO**
- Tipo de contenido: {content_type}
- Objetivo principal
- Mensaje clave

[ROUTER] **ESTRATEGIA**
- Por qué este approach funciona
- Alineación con marca Cafe.AI
- KPIs esperados

[OK] **APROBACIÓN**
- Elementos aprobados
- Ajustes recomendados (si los hay)
- Próximos pasos

[START] **PLAN DE EJECUCIÓN**
- Timeline
- Recursos necesarios
- Canales de distribución

Sé conciso pero completo. Este documento debe ser actionable."""
        },
        {
            "role": "user",
            "content": f"Revisa y aprueba la campaña {content_type} para Cafe.AI"
        }
    ]
    
    reply = llm.invoke(messages)
    
    print(f"\n{'='*60}")
    print(f"[SUPERVISOR AGENT] [SUPERVISOR]")
    print(f"Campaña final aprobada:")
    print(f"{reply.content[:200]}...")
    print(f"{'='*60}\n")
    
    return {
        "final_campaign": reply.content,
        "messages": [{"role": "assistant", "content": f"[SUPERVISOR] {reply.content}"}]
    }

########################################## CONDITIONAL ROUTING #####################################################

def route_after_router(state: MarketingState):
    """
    Decisión: después del router, siempre ir al creativo primero
    """
    return "creative"

def route_after_creative(state: MarketingState):
    """
    Decisión: después del creativo, ir al copywriter
    """
    return "copywriter"

def route_after_copywriter(state: MarketingState):
    """
    Decisión: después del copywriter, ir al diseñador
    """
    return "designer"

def route_after_designer(state: MarketingState):
    """
    Decisión: después del diseñador, ir al supervisor
    """
    return "supervisor"

########################################## GRAFO DE LANGGRAPH #####################################################

graph_builder = StateGraph(MarketingState)

# Agregar todos los nodos (agentes)
graph_builder.add_node("router", router_agent)
graph_builder.add_node("creative", creative_agent)
graph_builder.add_node("copywriter", copywriter_agent)
graph_builder.add_node("designer", designer_agent)
graph_builder.add_node("supervisor", supervisor_agent)

# Flujo: START → Router → Creative → Copywriter → Designer → Supervisor → END
graph_builder.add_edge(START, "router")

# Routing condicional (aunque en este caso es secuencial, podría ser condicional)
graph_builder.add_conditional_edges(
    "router",
    route_after_router,
    {"creative": "creative"}
)

graph_builder.add_conditional_edges(
    "creative",
    route_after_creative,
    {"copywriter": "copywriter"}
)

graph_builder.add_conditional_edges(
    "copywriter",
    route_after_copywriter,
    {"designer": "designer"}
)

graph_builder.add_conditional_edges(
    "designer",
    route_after_designer,
    {"supervisor": "supervisor"}
)

graph_builder.add_edge("supervisor", END)

# Compilar el grafo
graph = graph_builder.compile()

########################################## FUNCIÓN DE EJECUCIÓN #####################################################

def run_marketing_campaign():
    """
    Función principal para ejecutar el sistema de marketing
    """
    print("\n" + "="*80)
    print(" [START] SISTEMA DE MARKETING CAFE.AI - EQUIPO PUBLICITARIO [START] ")
    print("="*80)
    print("\nEquipo disponible:")
    print("  [ROUTER] Router - Clasifica tipo de contenido")
    print("  [CREATIVE] Creative - Genera conceptos creativos")
    print("  [COPYWRITER]  Copywriter - Escribe textos persuasivos")
    print("  [DESIGNER]  Designer - Crea briefs de diseño")
    print("  [SUPERVISOR] Supervisor - Revisa y aprueba campaña final")
    print("\n" + "="*80 + "\n")
    
    print("Ejemplos de solicitudes:")
    print("  - 'Crea un post para Instagram anunciando nuestra apertura'")
    print("  - 'Necesito un thread de Twitter sobre por qué Cafe.AI es diferente'")
    print("  - 'Diseña un anuncio de Facebook para atraer desarrolladores'")
    print("  - 'Crea una historia de Instagram mostrando el ambiente del café'")
    print("\n" + "="*80 + "\n")
    
    while True:
        user_input = input("> Describe la campaña que necesitas (o 'exit' para salir): ")
        
        if user_input.lower() == "exit":
            print("\n[BYE] ¡Hasta luego! Que tus campañas sean exitosas.\n")
            break
        
        if not user_input.strip():
            print("[WARNING]  Por favor ingresa una solicitud válida.\n")
            continue
        
        # Inicializar estado
        state = {
            "messages": [{"role": "user", "content": user_input}],
            "content_type": None,
            "creative_style": None,
            "priority": None,
            "creative_concept": None,
            "copy_text": None,
            "design_brief": None,
            "final_campaign": None,
            "route_to": None
        }
        
        print("\n" + "[PROCESSING] Procesando tu solicitud con el equipo completo...\n")
        
        # Ejecutar el grafo
        try:
            final_state = graph.invoke(state)
            
            # Mostrar resultado final
            print("\n" + "="*80)
            print(" * CAMPAÑA COMPLETA - LISTA PARA EJECUTAR * ")
            print("="*80 + "\n")
            
            if final_state.get("final_campaign"):
                print(final_state["final_campaign"])
            else:
                print("[WARNING]  No se pudo generar la campaña completa.")
            
            print("\n" + "="*80 + "\n")
            
            # Opción para guardar
            save = input("[SAVE] ¿Deseas guardar esta campaña en un archivo? (s/n): ")
            if save.lower() == 's':
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"campana_cafeai_{timestamp}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("="*80 + "\n")
                    f.write("CAMPAÑA DE MARKETING - CAFE.AI\n")
                    f.write(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("="*80 + "\n\n")
                    f.write(f"SOLICITUD:\n{user_input}\n\n")
                    f.write("="*80 + "\n\n")
                    f.write("CONCEPTO CREATIVO:\n")
                    f.write(final_state.get("creative_concept", "N/A") + "\n\n")
                    f.write("="*80 + "\n\n")
                    f.write("COPY:\n")
                    f.write(final_state.get("copy_text", "N/A") + "\n\n")
                    f.write("="*80 + "\n\n")
                    f.write("DESIGN BRIEF:\n")
                    f.write(final_state.get("design_brief", "N/A") + "\n\n")
                    f.write("="*80 + "\n\n")
                    f.write("APROBACIÓN FINAL:\n")
                    f.write(final_state.get("final_campaign", "N/A") + "\n\n")
                
                print(f"[OK] Campaña guardada en: {filename}\n")
            
        except Exception as e:
            print(f"\n[ERROR] Error al procesar la campaña: {str(e)}\n")
            continue
        
        print("\n" + "-"*80 + "\n")

########################################## FUNCIÓN DEMO #####################################################

def run_demo():
    """
    Función demo con ejemplos predefinidos
    """
    print("\n" + "="*80)
    print(" [DEMO] MODO DEMO - EJEMPLOS DE CAMPAÑAS CAFE.AI [DEMO] ")
    print("="*80 + "\n")
    
    demos = [
        "Crea un post de Instagram anunciando la gran apertura de Cafe.AI",
        "Necesito un thread de Twitter explicando por qué Cafe.AI es el mejor lugar para developers",
        "Diseña un anuncio de Facebook para atraer a la comunidad tech local"
    ]
    
    for i, demo_request in enumerate(demos, 1):
        print(f"\n{'='*80}")
        print(f" DEMO {i}/{len(demos)}: {demo_request}")
        print(f"{'='*80}\n")
        
        state = {
            "messages": [{"role": "user", "content": demo_request}],
            "content_type": None,
            "creative_style": None,
            "priority": None,
            "creative_concept": None,
            "copy_text": None,
            "design_brief": None,
            "final_campaign": None,
            "route_to": None
        }
        
        try:
            final_state = graph.invoke(state)
            
            if final_state.get("final_campaign"):
                print("\n" + "="*80)
                print(" * RESULTADO DEMO * ")
                print("="*80 + "\n")
                print(final_state["final_campaign"])
                print("\n" + "="*80 + "\n")
            
        except Exception as e:
            print(f"[ERROR] Error en demo: {str(e)}\n")
        
        if i < len(demos):
            input("\n[PAUSE]  Presiona Enter para continuar con el siguiente demo...")

########################################## MAIN #####################################################

if __name__ == "__main__":
    import sys
    
    # Intentar usar emojis, si falla usar texto simple
    try:
        cafe_emoji = "="
        test = cafe_emoji * 2
    except UnicodeEncodeError:
        cafe_emoji = "="
    
    print("\n" + cafe_emoji*40)
    print(" "*35 + "CAFE.AI")
    print(" "*20 + "Sistema de Marketing Multiagente")
    print(cafe_emoji*40 + "\n")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        run_marketing_campaign()
