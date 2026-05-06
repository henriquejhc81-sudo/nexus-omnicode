import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO DA PÁGINA E DESIGN CYBER-SENTINEL ---
st.set_page_config(page_title="Nexus Sentinel v5.4", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e0e0e0; }
    .stButton>button { 
        background: linear-gradient(135deg, #00c853 0%, #b2ff59 100%); 
        color: #000; font-weight: 800; border-radius: 8px; border: none; transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 200, 83, 0.3);
    }
    .status-box { 
        padding: 15px; border-radius: 10px; background: #161b22; 
        border: 1px solid #00c853; box-shadow: inset 0 0 10px rgba(0, 200, 83, 0.1);
        margin-bottom: 20px; font-family: 'Courier New', Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE IA COM BLINDAGEM E AUTOCORREÇÃO ---
def nexus_agent_call(prompt, modo, contexto):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return "Erro: Chave API ausente nos Secrets!"
        
    max_retries = 5
    for attempt in range(max_retries):
        try:
            # DIRETRIZ REORGANIZADA PARA FOCO EM CORREÇÃO AUTOMÁTICA
            prompt_sistema = f"""
            Você é o Nexus Sentinel 5.4. Missão: {modo}.
            
            REGRAS DE OURO:
            1. Se o modo for 'Varredura e Autocorreção', identifique TODOS os erros e gere o código 100% corrigido.
            2. Em QUALQUER projeto, inclua Módulo de Segurança e Logs de Invasão.
            3. Aplique Self-Healing (try/catch) em funções críticas.
            4. Responda com Guia de Setup, Estrutura de Pastas e Código Completo.
            """
            
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.1,
            )
            return completion.choices[0].message.content
            
        except Exception as e:
            if "429" in str(e):
                wait_time = (attempt + 1) * 8 
                st.warning(f"🛡️ Auto-Healing Anti-429: Aguardando {wait_time}s para sincronizar...")
                time.sleep(wait_time)
            else:
                return f"Erro Crítico: {e}"
    return "O Sentinel não pôde furar o bloqueio após 5 tentativas."

# --- BARRA LATERAL REORGANIZADA ---
with st.sidebar:
    st.title("🛡️ Nexus Sentinel")
    st.caption("v5.4 | Elite Intelligence")
    
    st.divider()
    with st.expander("🚀 Superpoderes Sentinel", expanded=True):
        st.toggle("Segurança Nativa", value=True)
        st.toggle("Auto-Healing Anti-429", value=True)
        st.toggle("Modo Arquiteto Ativo", value=True)
        st.toggle("Live Preview", value=True)

    st.divider()
    st.subheader("🔗 DevSecOps")
    for app in ["GitLab", "GitHub", "Azure DevOps", "Slack/Notion"]:
        st.toggle(app, value=True)
    
    # NOVA FUNÇÃO DE VARREDURA ADICIONADA
    modo = st.selectbox("🎯 Modo do Agente", [
        "Varredura e Autocorreção Automática",
        "Projeto do Zero (Modo Arquiteto)",
        "Incremento Mágico + Segurança",
        "Análise de Vulnerabilidades (Snyk)",
        "Design-to-Code Cyber Neon"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus OmniCode Sentinel")
st.markdown("<div class='status-box'><b>SENTINEL:</b> VIGILANTE | <b>AUTO-HEALING:</b> ATIVO | <b>VARREDURA:</b> LIGADA</div>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📥 Entrada de Missão")
    user_input = st.text_area("Cole seu código com erro ou descreva sua ideia:", height=300)
    upload = st.file_uploader("Contexto Adicional", accept_multiple_files=True)

with col_out:
    st.subheader("🚀 Resposta do Sentinel")
    if st.button("ATIVAR NEXUS SENTINEL"):
        if user_input:
            with st.spinner("Sentinel realizando varredura e gerando blindagem..."):
                try:
                    with DDGS() as ddgs:
                        busca = [r['body'] for r in ddgs.text(f"security and debugging best practices for {user_input}", max_results=2)]
                        contexto = "\n".join(busca)
                except:
                    contexto = "Usando base interna de elite."
                
                resultado = nexus_agent_call(user_input, modo, contexto)
                st.session_state['last_result'] = resultado
        else:
            st.error("O Sentinel aguarda seus dados.")

    if 'last_result' in st.session_state:
        res = st.session_state['last_result']
        tab1, tab2 = st.tabs(["💻 Plano e Código", "🖼️ Live Preview"])
        with tab1:
            st.markdown(res)
        with tab2:
            if "<html>" in res.lower() or "<!doctype html>" in res.lower():
                st.components.v1.html(res, height=500, scrolling=True)
            else:
                st.info("O Live Preview aguarda código HTML.")

        st.divider()
        ext = st.selectbox("Formato:", [".py", ".html", ".js", ".txt"], key="fmt")
        st.download_button(label=f"BAIXAR PROJETO ({ext})", data=res, file_name=f"nexus_sentinel_v54{ext}")

# --- CHAT SUPORTE ---
st.divider()
st.subheader("💬 Nexus Sentinel Chat Pro")
chat_input = st.text_input("Dúvida técnica ou pedido de ajuste?")
if chat_input and 'last_result' in st.session_state:
    with st.chat_message("assistant"):
        st.markdown(nexus_agent_call(f"Contexto: {st.session_state['last_result']}. Pergunta: {chat_input}", "Chat Suporte", ""))
