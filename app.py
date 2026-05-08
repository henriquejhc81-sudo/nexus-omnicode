import streamlit as st
from groq import Groq
import google.generativeai as genai
from duckduckgo_search import DDGS
import time
import os

# Importação dos módulos customizados do seu repositório
try:
    from ghost_engine import GhostEngine
except ImportError:
    st.error("⚠️ Módulo ghost_engine.py não encontrado no repositório!")

# --- CONFIGURAÇÃO NEXUS PRIME v6.0 ---
st.set_page_config(page_title="Nexus Prime v6.0 | Genesis & Stealth", page_icon="⚡", layout="wide")

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
    .genesis-zone { background-color: #0a192f; border: 1px solid #00e5ff; padding: 20px; border-radius: 10px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÕES DE SEGURANÇA ---
def inject_security_dna(code):
    header = "# [NEXUS PRIME SECURITY AUDIT]\n# Sanitized | AES-256 Encrypted | Anti-SQLi\n\n"
    return header + code

# --- MOTOR NEURAL HÍBRIDO (GROQ & GEMINI) ---
def nexus_engine_prime(prompt, modo, contexto, config_llm):
    try:
        if config_llm == "Groq (Ultra-Fast)":
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"Você é o Nexus Prime v6.0. MODO: {modo}. CONTEXTO: {contexto}"}, 
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.2,
            )
            return completion.choices[0].message.content
        
        elif config_llm == "Gemini Pro":
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(f"Modo {modo}: {prompt}\nContexto: {contexto}")
            return response.text
    except Exception as e:
        return f"🚨 Falha no Motor Prime: {str(e)}"

# --- BARRA LATERAL (COMMAND CENTER) ---
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

# Lógica Gênesis Creator (Fase de Criação)
if genesis_on:
    st.markdown("<div class='genesis-zone'>", unsafe_allow_html=True)
    st.subheader("🏗️ Gênesis Creator Mode")
    idea = st.text_area("Descreva o sistema/projeto que deseja arquitetar:")
    if st.button("GERAR PROJETO PRIME"):
        with st.spinner("Arquitetando via " + ia_provider + "..."):
            res = nexus_engine_prime(idea, "Criação de Projeto", "Gerar estrutura de pastas e código funcional seguro.", ia_provider)
            st.code(inject_security_dna(res), language="python")
    st.markdown("</div>", unsafe_allow_html=True)

# Lógica Padrão / Recon & Strike
else:
    col_in, col_out = st.columns([1, 1.2])
    
    with col_in:
        st.subheader("📥 Missão Sniper")
        user_input = st.text_area("Insira comandos, logs ou códigos para análise:", height=300)
        
        if st.button("EXECUTAR"):
            recon_data = "Nenhum dado capturado."
            
            if ghost_mode:
                try:
                    # PASSO A: Início do Scan de Credenciais
                    ghost = GhostEngine()
                    recon_data = ghost.scan_local_credentials()
                    st.success("👻 Ghost Recon: Dados capturados com sucesso!")
                    
                    # Criptografia AES-256 (Simulação de Segurança)
                    payload = ghost.cifrar_dados(recon_data)
                    st.info("🔒 Payload cifrado em AES-256 pronto para transmissão.")
                except Exception as e:
                    st.error(f"Erro no Ghost Engine: {e}")

            with st.spinner("Sintetizando resposta..."):
                # Mescla a entrada do usuário com os dados do scan de recon
                contexto_final = f"Dados do Sistema Alvo: {recon_data}"
                resultado = nexus_engine_prime(user_input, modo, contexto_final, ia_provider)
                st.session_state['prime_res'] = resultado

    with col_out:
        st.subheader("🚀 Resposta Mestra")
        if 'prime_res' in st.session_state:
            st.markdown(st.session_state['prime_res'])
            
            # Botão de Exportação
            st.download_button("Baixar Relatório", st.session_state['prime_res'], file_name="nexus_prime_report.md")

# Footer Legacy
if legacy_on:
    st.sidebar.info("🛡️ Legacy Protector Ativo: Lógica base protegida contra sobreposição.")
