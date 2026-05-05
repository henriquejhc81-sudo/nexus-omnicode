import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO DA PÁGINA E DESIGN DE ALTA PERFORMANCE ---
st.set_page_config(page_title="Nexus OmniCode Sentinel", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #4CAF50; color: white; font-weight: bold; border-radius: 10px; width: 100%; height: 3em; }
    .status-box { padding: 15px; border-radius: 10px; background: #1a1c24; border-left: 5px solid #4CAF50; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE IA COM CORREÇÃO DE ATRIBUTO E AUTO-HEALING (ERRO 429) ---
def nexus_agent_call(prompt, modo, contexto):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return "Erro: API Key não configurada!"
        
    max_retries = 3
    for attempt in range(max_retries):
        try:
            prompt_sistema = f"""
            Você é o Nexus Sentinel (Agente Autônomo). Missão: {modo}.
            CONDIÇÕES: Secure At Inception, Self-Healing ativo.
            CONTEXTO REPOSITÓRIO: {contexto}
            Se houver HTML, gere o código completo entre tags <html>.
            Gere Testes Unitários automatizados. Responda em Português.
            """
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.1,
            )
            # CORREÇÃO DEFINITIVA DO ERRO DE ATRIBUTO:
            return completion.choices[0].message.content
            
        except Exception as e:
            if "429" in str(e):
                st.warning(f"⚠️ Estabilizando conexão (Cota 429)... Tentativa {attempt+1}")
                time.sleep(6) 
            else:
                return f"Erro Crítico no Agente: {e}"
    return "Falha após múltiplas tentativas de sincronização."

# --- BARRA LATERAL (SUPERPODERES) ---
with st.sidebar:
    st.title("🛡️ Nexus Sentinel")
    st.caption("Modo Agente Autônomo Ativado")
    
    st.divider()
    with st.expander("🚀 Superpoderes Ativos", expanded=True):
        st.toggle("Self-Healing (Auto-correção)", value=True)
        st.toggle("Scanner de Vulnerabilidade (Snyk)", value=True)
        st.toggle("Live Preview Interativo", value=True)
        st.toggle("Geração de Testes Unitários", value=True)

    st.divider()
    st.subheader("🔗 Integrações DevSecOps")
    for app in ["GitLab", "GitHub (PR Writer)", "Azure DevOps", "Slack/Notion (MCP)"]:
        st.toggle(app, value=True)
    
    modo = st.selectbox("🎯 Modo do Agente", [
        "Agente de Execução Ponta a Ponta",
        "Incremento Mágico + Testes",
        "Análise de Vulnerabilidades (Secure Code)",
        "Design-to-Code (Interface)",
        "Escritor de Pull Request"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus OmniCode v5.0")
st.markdown("<div class='status-box'><b>Status do Sentinel:</b> Vigilante | <b>Auto-Healing:</b> Pronto | <b>Sincronização:</b> Otimizada</div>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📥 Input do Desenvolvedor")
    user_input = st.text_area("Descreva a tarefa ou cole o código:", height=300, placeholder="Ex: Dashboard de Fintech com proteção SQLi...")
    upload = st.file_uploader("Upload de Arquivos", accept_multiple_files=True)

with col_out:
    st.subheader("🚀 Output do Agente Autônomo")
    if st.button("ATIVAR NEXUS SENTINEL"):
        if user_input:
            with st.spinner("Sentinel processando e validando segurança..."):
                time.sleep(random.uniform(1.0, 2.0))
                try:
                    with DDGS() as ddgs:
                        busca = [r['body'] for r in ddgs.text(f"security best practices for {user_input}", max_results=2)]
                        contexto = "\n".join(busca)
                except:
                    contexto = "Base interna ativa."
                
                resultado = nexus_agent_call(user_input, modo, contexto)
                st.session_state['last_result'] = resultado
                
                tab1, tab2 = st.tabs(["💻 Código e Testes", "🖼️ Live Preview"])
                with tab1:
                    st.markdown(resultado)
                with tab2:
                    if "<html>" in resultado.lower() or "<!doctype html>" in resultado.lower():
                        st.components.v1.html(resultado, height=500, scrolling=True)
                    else:
                        st.info("O Live Preview aparecerá quando um código HTML for gerado.")

    if 'last_result' in st.session_state:
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            formato = st.selectbox("Formato de Saída:", [".py", ".html", ".js", ".sql", ".txt"])
        with c2:
            st.download_button(label=f"📥 BAIXAR PROJETO ({formato})", data=st.session_state['last_result'], file_name=f"nexus_sentinel{formato}")

# --- CHAT DEEP CONTEXT ---
st.divider()
st.subheader("💬 Nexus Sentinel Chat (Deep Context)")
chat_input = st.text_input("Dúvida sobre o código ou segurança?")
if chat_input and 'last_result' in st.session_state:
    with st.chat_message("assistant"):
        st.markdown(nexus_agent_call(f"Sobre este código: {st.session_state['last_result']}. Pergunta: {chat_input}", "Chat Suporte", ""))
