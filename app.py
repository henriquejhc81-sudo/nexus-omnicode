import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO NEXUS SENTINEL v5.5 "DEEP BRAIN" ---
st.set_page_config(page_title="Nexus Sentinel v5.5 | Deep Brain", page_icon="🛡️", layout="wide")

# CSS - Interface de Centro de Comando Cibernético
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e0e0e0; }
    .stButton>button { 
        background: linear-gradient(135deg, #00c853 0%, #b2ff59 100%); 
        color: #000; font-weight: 800; border-radius: 8px; border: none; height: 3.5em;
        box-shadow: 0 4px 15px rgba(0, 200, 83, 0.4);
    }
    .status-box { 
        padding: 15px; border-radius: 10px; background: #161b22; 
        border: 1px solid #00c853; box-shadow: inset 0 0 15px rgba(0, 200, 83, 0.2);
        margin-bottom: 20px; font-family: 'Courier New', Courier, monospace;
    }
    .risk-score { font-size: 24px; font-weight: bold; color: #ff5252; }
    </style>
    """, unsafe_allow_html=True)

# --- HEALER ENGINE & MOTOR NEURAL (ANTI-LOCK 429) ---
def nexus_deep_brain(prompt, modo, contexto):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return "⚠️ Erro: Motor Neural sem Chave API nos Secrets!"
        
    for attempt in range(5):
        try:
            # ORQUESTRAÇÃO MULTI-IA: Simula 7 perspectivas
            prompt_sistema = f"""
            Você é o Nexus Sentinel 5.5 'Deep Brain'. Use os motores Gemini 1.5 Pro e Flash.
            MISSÃO: {modo}. CONTEXTO: {contexto}.
            
            DIRETRIZES DE ELITE:
            1. [Orquestração]: Simule 7 especialistas para chegar à Conclusão Mestra.
            2. [Segurança]: Inclua Matriz de Risco (0-100%) e Logs de Invasão.
            3. [Due Diligence]: Varredura massiva para identificar anomalias e 'agulhas no palheiro'.
            4. [Healer]: Se houver erro, aplique Self-Healing (Auto-Cura).
            5. [Arquiteto]: Setup, Estrutura de Pastas e Código Completo.
            6. [Tradução]: Mantenha tradução técnica global integrada.
            """
            
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile", # Groq Engine agindo como ponte para orquestração
                temperature=0.1,
            )
            return completion.choices[0].message.content
            
        except Exception as e:
            if "429" in str(e):
                wait = (attempt + 1) * 8
                st.warning(f"🛡️ Healer Engine Ativo: Reconectando rota estável em {wait}s...")
                time.sleep(wait)
            else:
                return f"Falha no Motor Neural: {e}"
    return "Sentinel offline após 5 tentativas. Verifique a cota."

# --- BARRA LATERAL (CENTRO DE COMANDO) ---
with st.sidebar:
    st.title("🛡️ NEXUS SENTINEL")
    st.caption("v5.5 | DEEP BRAIN EDITION")
    
    with st.expander("👁️ Sentinel Visual", expanded=True):
        st.toggle("Neural Sniper Prompt", value=True)
        st.toggle("Data Processing (Any File)", value=True)
        st.toggle("Computer Vision (Simulado)", value=True)
        st.toggle("Forensic Analytics", value=True)

    st.divider()
    st.subheader("🛠️ Deep Learning Engine")
    for tool in ["Due Diligence Automática", "E-Discovery", "Historic Learning", "Matriz de Risco"]:
        st.toggle(tool, value=True)
    
    st.divider()
    modo = st.selectbox("🎯 Neural Sniper Target", [
        "Varredura e Autocorreção Automática",
        "Due Diligence e Matriz de Risco",
        "E-Discovery (Busca Massiva)",
        "Projeto do Zero (Modo Arquiteto)",
        "Incremento Mágico + Tradução Global"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus Sentinel v5.5")
st.markdown("""
<div class='status-box'>
    <b>MOTOR:</b> GEMINI 1.5 PRO / FLASH | <b>STATUS:</b> VIGILANTE | <b>HEALER ENGINE:</b> ONLINE
</div>
""", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📥 Neural Sniper Input")
    user_input = st.text_area("Insira o comando ou cole a base de dados complexa:", height=300)
    upload = st.file_uploader("Data Processing: Carregar base de dados", accept_multiple_files=True)

with col_out:
    st.subheader("🚀 Output Mestre (7 Perspectivas)")
    if st.button("ATIVAR NEXUS SENTINEL"):
        if user_input:
            with st.spinner("Motor Deep Brain processando 1 milhão de tokens e simulando perspectivas..."):
                try:
                    with DDGS() as ddgs:
                        busca = [r['body'] for r in ddgs.text(f"forensic and statistical analysis for {user_input}", max_results=3)]
                        contexto = "\n".join(busca)
                except:
                    contexto = "Usando Historic Learning interno."
                
                resultado = nexus_deep_brain(user_input, modo, contexto)
                st.session_state['last_result'] = resultado
        else:
            st.error("O Sentinel aguarda um alvo neural.")

    if 'last_result' in st.session_state:
        res = st.session_state['last_result']
        tab1, tab2 = st.tabs(["💻 Código e Análise Forense", "🖼️ Live Preview"])
        with tab1:
            st.markdown(res)
        with tab2:
            if "<html>" in res.lower() or "<!doctype html>" in res.lower():
                st.components.v1.html(res, height=550, scrolling=True)
            else:
                st.info("O Live Preview aguarda código visual.")

        # EXPORTAÇÃO MULTIFORMATO
        st.divider()
        ext = st.selectbox("Exportar como Relatório Executivo:", [".py", ".html", ".docx", ".js", ".txt"])
        st.download_button(label=f"📥 BAIXAR OUTPUT ({ext})", data=res, file_name=f"nexus_deep_brain_report{ext}")

# --- CHAT SUPORTE ---
st.divider()
st.subheader("💬 Nexus Sentinel Chat (Deep Context)")
chat_input = st.text_input("Dúvida sobre a Matriz de Risco ou Código?")
if chat_input and 'last_result' in st.session_state:
    with st.chat_message("assistant"):
        st.markdown(nexus_deep_brain(f"Sobre este projeto: {st.session_state['last_result']}. Responda: {chat_input}", "Chat Suporte", ""))
