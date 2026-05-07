import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO NEXUS SENTINEL v5.8 "ADVERSARY PRO" ---
st.set_page_config(page_title="Nexus Sentinel v5.8 | Adversary Pro", page_icon="🛡️", layout="wide")

# CSS - Centro de Comando Cibernético de Elite
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
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR NEURAL COM CORREÇÃO DE ATRIBUTO E SIMULAÇÃO ADVERSÁRIA ---
def nexus_adversary_brain(prompt, modo, contexto, dna_ativo, adversary_ativo):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return "⚠️ Erro Crítico: Chave API ausente!"
        
    for attempt in range(5):
        try:
            time.sleep(random.uniform(0.5, 1.5)) 
            
            dna_prompt = "INJEÇÃO DNA NEXUS ATIVA: Motor Neural, Ghost AI e Segurança Integral." if dna_ativo else ""
            adversary_prompt = ""
            if adversary_ativo:
                adversary_prompt = """
                ALERTA: SIMULAÇÃO ADVERSÁRIA ATIVA.
                Proteja contra: 1. Predição (GANs), 2. Infostealers, 3. Phishing (Evilginx2), 4. Credential Stuffing.
                """

            prompt_sistema = f"Você é o Nexus Sentinel 5.8. MISSÃO: {modo}. {dna_prompt} {adversary_prompt} CONTEXTO: {contexto}."
            
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.2,
            )
            # CORREÇÃO DEFINITIVA PARA EVITAR O ERRO 'list' object
            return completion.choices[0].message.content
            
        except Exception as e:
            if "429" in str(e):
                wait = (attempt + 1) * 8
                st.warning(f"🛡️ Healer Engine: Reconectando em {wait}s...")
                time.sleep(wait)
            else:
                return f"Falha no Motor Adversário: {e}"
    return "Sentinel Offline após falhas de sincronização."

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🛡️ NEXUS SENTINEL")
    st.caption("v5.8 | ADVERSARY PRO")
    
    with st.expander("🧬 DNA & Adversário", expanded=True):
        dna_ativo = st.toggle("Injetar DNA Nexus", value=True)
        adversary_ativo = st.toggle("Simulação Adversária", value=True)
        st.toggle("Human-Mimic Mode", value=True)

    st.divider()
    st.subheader("🛠️ Forensic Intelligence")
    for tool in ["Due Diligence", "E-Discovery", "Matriz de Risco", "Forensic Analytics"]:
        st.toggle(tool, value=True)
    
    modo = st.selectbox("🎯 Neural Target", [
        "Simulação de Ataque e Defesa",
        "Projeto do Zero (Modo Arquiteto)",
        "Due Diligence e Matriz de Risco",
        "Incremento Mágico + Adversário",
        "E-Discovery (Busca Invisível)"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus Sentinel v5.8")
st.markdown(f"<div class='status-box'><b>STATUS:</b> VIGILANTE | <b>ADVERSÁRIO:</b> {'ATIVA' if adversary_ativo else 'OFF'} | <b>DNA:</b> {'INJETADO' if dna_ativo else 'OFF'}</div>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📥 Missão Sniper")
    user_input = st.text_area("Descreva o projeto (A blindagem adversária será aplicada):", height=300)
    upload = st.file_uploader("Upload de Contexto", accept_multiple_files=True)

with col_out:
    st.subheader("🚀 Resposta Mestra Adversária")
    if st.button("ATIVAR NEXUS SENTINEL"):
        if user_input:
            with st.spinner("Motor Adversário simulando ataques e gerando blindagem..."):
                try:
                    with DDGS() as ddgs:
                        busca = [r['body'] for r in ddgs.text(f"cybersecurity best practices 2026: {user_input}", max_results=2)]
                        contexto = "\n".join(busca)
                except:
                    contexto = "Base interna ativa."
                
                resultado = nexus_adversary_brain(user_input, modo, contexto, dna_ativo, adversary_ativo)
                st.session_state['last_result'] = resultado
        else:
            st.error("Insira o alvo da missão.")

    if 'last_result' in st.session_state:
        res = st.session_state['last_result']
        tab1, tab2 = st.tabs(["💻 Código Blindado", "🖼️ Live Preview"])
        with tab1:
            st.markdown(res)
        with tab2:
            if "<html>" in res.lower() or "<!doctype html>" in res.lower():
                st.components.v1.html(res, height=550, scrolling=True)
            else:
                st.info("Aguardando interface visual.")

        st.divider()
        ext = st.selectbox("Exportar como:", [".html", ".py", ".docx", ".txt"])
        st.download_button(label=f"📥 BAIXAR PROJETO ({ext})", data=res, file_name=f"nexus_adversary_output{ext}")

# --- CHAT ---
st.divider()
st.subheader("💬 Nexus Ghost Chat")
chat_input = st.text_input("Dúvida sobre a proteção adversária?")
if chat_input and 'last_result' in st.session_state:
    with st.chat_message("assistant"):
        st.markdown(nexus_adversary_brain(f"Sobre este projeto: {st.session_state['last_result']}. Pergunta: {chat_input}", "Chat Support", "", dna_ativo, adversary_ativo))
