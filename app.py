import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO DA PÁGINA E DESIGN CYBER-SENTINEL ---
st.set_page_config(page_title="Nexus Sentinel v5.2", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e0e0e0; }
    .stButton>button { 
        background: linear-gradient(135deg, #00c853 0%, #b2ff59 100%); 
        color: #000; font-weight: 800; border-radius: 8px; border: none; transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 200, 83, 0.3);
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 200, 83, 0.5); }
    .stTextArea>div>div>textarea { background-color: #161b22; color: #ffffff; border: 1px solid #30363d; border-radius: 8px; }
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .status-box { 
        padding: 15px; border-radius: 10px; background: #161b22; 
        border: 1px solid #00c853; box-shadow: inset 0 0 10px rgba(0, 200, 83, 0.1);
        margin-bottom: 20px; font-family: 'Courier New', Courier, monospace;
    }
    .guide-box { background-color: #1a1c24; padding: 15px; border-radius: 10px; border-left: 5px solid #00c853; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE IA COM CORREÇÃO DE ATRIBUTO E AUTO-HEALING ---
def nexus_agent_call(prompt, modo, contexto):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return "Erro: API Key não configurada!"
        
    max_retries = 3
    for attempt in range(max_retries):
        try:
            prompt_sistema = f"""
            Você é o Nexus Sentinel 5.2. Missão: {modo}.
            CONDIÇÕES: Secure At Inception, Self-Healing ativo.
            
            NOVA DIRETRIZ (MODO ARQUITETO):
            Se for um projeto do zero, você DEVE começar com:
            1. '🛠️ SETUP': Quais programas instalar.
            2. '📁 ESTRUTURA': Desenho das pastas.
            3. '🚀 CÓDIGO': O código completo.
            
            Responda em Português com foco em ser didático para leigos.
            """
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.1,
            )
            # CORREÇÃO DO ERRO 'list' object has no attribute 'message'
            return completion.choices[0].message.content
            
        except Exception as e:
            if "429" in str(e):
                st.warning(f"⚠️ Estabilizando conexão (Cota 429)... Tentativa {attempt+1}")
                time.sleep(6) 
            else:
                return f"Erro Crítico: {e}"
    return "Falha após múltiplas tentativas de sincronização."

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🛡️ Nexus Sentinel")
    st.caption("v5.2 | Architect Mode")
    
    st.divider()
    with st.expander("🚀 Superpoderes Ativos", expanded=True):
        st.toggle("Modo Arquiteto (Guia Iniciante)", value=True)
        st.toggle("Self-Healing", value=True)
        st.toggle("Live Preview", value=True)
        st.toggle("Unit Tests", value=True)

    st.divider()
    st.subheader("🔗 DevSecOps")
    for app in ["GitLab", "GitHub", "Azure DevOps", "Slack/Notion"]:
        st.toggle(app, value=True)
    
    modo = st.selectbox("🎯 Modo do Agente", [
        "Projeto do Zero (Modo Arquiteto)",
        "Incremento Mágico + Testes",
        "Análise de Vulnerabilidades",
        "Design-to-Code",
        "Escritor de Pull Request"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus OmniCode Sentinel")
st.markdown("<div class='status-box'><b>STATUS:</b> ONLINE | <b>MODO:</b> ARQUITETO | <b>MEMÓRIA:</b> ANCORADA</div>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📥 Missão")
    user_input = st.text_area("Descreva o que quer criar (até leigos conseguem agora!):", height=300, placeholder="Ex: Quero um site de vendas de carros...")
    upload = st.file_uploader("Arquivos de Contexto", accept_multiple_files=True)

with col_out:
    st.subheader("🚀 Entrega Sentinel")
    if st.button("ATIVAR NEXUS SENTINEL"):
        if user_input:
            with st.spinner("Sentinel traçando o plano arquitetônico..."):
                try:
                    with DDGS() as ddgs:
                        busca = [r['body'] for r in ddgs.text(f"best project structure for {user_input}", max_results=2)]
                        contexto = "\n".join(busca)
                except:
                    contexto = "Base interna ativa."
                
                resultado = nexus_agent_call(user_input, modo, contexto)
                st.session_state['last_result'] = resultado
        else:
            st.error("Diga ao Nexus o que você deseja construir.")

    if 'last_result' in st.session_state:
        resultado = st.session_state['last_result']
        
        tab1, tab2 = st.tabs(["💻 Plano e Código", "🖼️ Live Preview"])
        with tab1:
            st.markdown(resultado)
        with tab2:
            if "<html>" in resultado.lower() or "<!doctype html>" in resultado.lower():
                st.components.v1.html(resultado, height=500, scrolling=True)
            else:
                st.info("O Live Preview mostrará a interface assim que o código HTML for gerado.")

        st.divider()
        st.subheader("📥 Exportação")
        c1, c2 = st.columns(2)
        with c1:
            formato_ext = st.selectbox("Escolha o formato:", [".py", ".html", ".js", ".sql", ".txt"], key="formato_selector")
        with c2:
            st.download_button(
                label=f"BAIXAR PROJETO ({formato_ext})",
                data=resultado,
                file_name=f"nexus_sentinel_project{formato_ext}",
                mime="text/plain"
            )

# --- CHAT DEEP CONTEXT ---
st.divider()
st.subheader("💬 Nexus Sentinel Chat")
chat_input = st.text_input("Não entendeu algum passo? Pergunte ao Sentinel:")
if chat_input and 'last_result' in st.session_state:
    with st.chat_message("assistant"):
        st.markdown(nexus_agent_call(f"Sobre este projeto: {st.session_state['last_result']}. Pergunta: {chat_input}", "Chat Suporte", ""))
