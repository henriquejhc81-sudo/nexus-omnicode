import streamlit as st
from groq import Groq
import google.generativeai as genai
import os

# Importação do motor evoluído
try:
    from ghost_engine import GhostEngine
except ImportError:
    st.error("Módulo ghost_engine.py ausente!")

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Nexus Prime v6.1", page_icon="⚡", layout="wide")

# CSS Cyber-Neon
st.markdown("""
    <style>
    .main { background-color: #05070a; color: #e0e0e0; }
    .stButton>button { background: linear-gradient(135deg, #00e5ff 0%, #1200ff 100%); color: #fff; border: none; height: 3em; }
    .status-box { padding: 10px; border-radius: 10px; background: #0d1117; border: 1px solid #00e5ff; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE NEURAL ---
def nexus_engine_prime(prompt, modo, contexto, engine):
    try:
        if engine == "Groq (Ultra-Fast)":
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            comp = client.chat.completions.create(
                messages=[{"role": "system", "content": f"Nexus Prime. Modo: {modo}. Contexto: {contexto}"}, 
                          {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile", temperature=0.2)
            return comp.choices[0].message.content
        else:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel('gemini-pro')
            return model.generate_content(f"{modo}: {prompt} \nContexto: {contexto}").text
    except Exception as e:
        return f"Erro: {e}"

# --- INTERFACE ---
with st.sidebar:
    st.title("⚡ NEXUS PRIME v6.1")
    ghost_mode = st.toggle("Ghost Stealth (AES-256)", value=False)
    ia_provider = st.selectbox("Neural Engine", ["Groq (Ultra-Fast)", "Gemini Pro"])
    modo = st.selectbox("Target", ["Recon", "Strike", "Genesis"])

st.title("🚀 Nexus Prime Engine")
st.markdown(f"<div class='status-box'>STATUS: ONLINE | GHOST: {'ATIVO' if ghost_mode else 'OFF'}</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2])

with col1:
    user_input = st.text_area("Comandos ou Logs:", height=300)
    if st.button("EXECUTAR"):
        full_recon = ""
        if ghost_mode:
            try:
                ghost = GhostEngine()
                # Executa Passo A e Passo B
                data_a = ghost.scan_local_credentials()
                data_b = ghost.shadow_cookie_scan()
                full_recon = f"{data_a} | {data_b}"
                st.success("👻 Ghost Recon & Shadow-Cookie Ativados!")
            except Exception as e:
                st.error(f"Falha no Ghost: {e}")
        
        with st.spinner("Sintetizando..."):
            res = nexus_engine_prime(user_input, modo, full_recon, ia_provider)
            st.session_state['res'] = res

with col2:
    if 'res' in st.session_state:
        st.markdown(st.session_state['res'])
