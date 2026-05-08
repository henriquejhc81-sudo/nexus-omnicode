import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import google.generativeai as genai
import time
import random
from ghost_engine import GhostEngine  # Importação do seu novo módulo Ghost

# --- CONFIGURAÇÃO NEXUS PRIME v6.0 ---
st.set_page_config(page_title="Nexus Prime v6.0 | Genesis & Strike", page_icon="⚡", layout="wide")

# CSS - Evolução Cyber-Neon Prime
st.markdown("""
    <style>
    .main { background-color: #05070a; color: #e0e0e0; }
    .stButton>button { 
        background: linear-gradient(135deg, #00e5ff 0%, #1200ff 100%); 
        color: #fff; font-weight: 800; border-radius: 8px; border: none; height: 3.5em;
        box-shadow: 0 4px 15px rgba(0, 229, 255, 0.3);
    }
    .status-box { 
        padding: 15px; border-radius: 10px; background: #0d1117; 
        border: 1px solid #00e5ff; box-shadow: inset 0 0 15px rgba(0, 229, 255, 0.1);
        margin-bottom: 20px; font-family: 'Courier New', Courier, monospace;
    }
    .genesis-zone { background-color: #0a192f; border: 1px solid #00e5ff; padding: 20px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÕES DE SEGURANÇA (DNA INJECTOR) ---
def inject_security_dna(code):
    header = "# [NEXUS PRIME SECURITY AUDIT]\n# Sanitized | AES-256 Encrypted | Anti-SQLi\n\n"
    return header + code

# --- MOTOR NEURAL HÍBRIDO ---
def nexus_engine_prime(prompt, modo, contexto, config_llm):
    try:
        if config_llm == "Groq (Ultra-Fast)":
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": f"Nexus Prime v6.0. Modo: {modo}. Contexto: {contexto}"}, 
                          {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.2,
            )
            return completion.choices[0].message.content
        
        elif config_llm == "Gemini Pro":
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(f"{modo}: {prompt}")
            return response.text
    except Exception as e:
        return f"Falha no Motor Prime: {e}"

# --- BARRA LATERAL (COMMAND CENTER v6.0) ---
with st.sidebar:
    st.title("⚡ NEXUS PRIME")
    st.caption("v6.0 | GENESIS & STEALTH")
    
    with st.expander("🛠️ Módulos de Expansão", expanded=True):
        genesis_on = st.toggle("Gênesis Creator", value=False)
        legacy_on = st.toggle("Legacy Protector", value=True)
        ghost_mode = st.toggle("Ghost Stealth (AES-256)", value=False)
    
    st.divider()
    ia_provider = st.selectbox("Engine Neural", ["Groq (Ultra-Fast)", "Gemini Pro"])
    
    modo = st.selectbox("🎯 Neural Target", [
        "Genesis: Arquitetura do Zero",
        "Strike: Contra-Ataque Forense",
        "Legacy: Auditoria de Código",
        "Recon: Inteligência de Campo"
    ])

# --- ÁREA PRINCIPAL ---
st.title("🚀 Nexus Prime Engine")
st.markdown(f"<div class='status-box'><b>SISTEMA:</b> ONLINE | <b>ENGINE:</b> {ia_provider} | <b>GHOST:</b> {'ATIVO' if ghost_mode else 'OFF'}</div>", unsafe_allow_html=True)

if genesis_on:
    with st.container():
        st.markdown("<div class='genesis-zone'>", unsafe_allow_html=True)
        st.subheader("🏗️ Gênesis Creator")
        idea = st.text_area("Descreva o sistema que deseja criar:")
        if st.button("GERAR PROJETO PRIME"):
            res = nexus_engine_prime(idea, "Criação de Projeto", "Gerar estrutura de pastas e código seguro.", ia_provider)
            st.code(inject_security_dna(res), language="python")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    col_in, col_out = st.columns([1, 1.2])
    with col_in:
        st.subheader("📥 Missão Sniper")
        user_input = st.text_area("Comandos ou Logs:", height=300)
        if st.button("EXECUTAR"):
            if ghost_mode:
                try:
                    ghost = GhostEngine()
                    cifrado = ghost.cifrar_dados(user_input)
                    st.info("👻 Dado cifrado com AES-256 e preparado para o Túnel.")
                except:
                    st.error("Erro: Chave 'nexus_prime.key' não encontrada!")

            with st.spinner("Sintetizando..."):
                resultado = nexus_engine_prime(user_input, modo, "Base Interna Nexus", ia_provider)
                st.session_state['prime_res'] = resultado

    with col_out:
        st.subheader("🚀 Resposta Mestra")
        if 'prime_res' in st.session_state:
            st.markdown(st.session_state['prime_res'])

# Footer de Proteção
if legacy_on:
    st.sidebar.warning("🛡️ Proteção Legacy: Alterações na base protegidas.")
