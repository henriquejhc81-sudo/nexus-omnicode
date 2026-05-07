import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO NEXUS SENTINEL v5.9 "RECON & STRIKE" ---
st.set_page_config(page_title="Nexus Sentinel v5.9 | Recon & Strike", page_icon="🛡️", layout="wide")

# CSS - Interface de Comando de Elite
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
    .strike-zone { background-color: #2b0b0b; border: 1px solid #ff5252; padding: 10px; border-radius: 8px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR NEURAL v5.9 COM PROTOCOLO DE DENÚNCIA ---
def nexus_recon_strike(prompt, modo, contexto, dna_ativo, adversary_ativo, strike_ativo):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return "⚠️ Erro Crítico: Motor fora de linha!"
        
    for attempt in range(5):
        try:
            time.sleep(random.uniform(0.5, 1.2)) 
            
            # Construção da Lógica de Comando
            dna_prompt = "INJEÇÃO DNA NEXUS: Motor Neural, Ghost AI e Blindagem Total." if dna_ativo else ""
            adversary_prompt = "SIMULAÇÃO ADVERSÁRIA: GANs, Infostealers, Phishing e Credential Stuffing." if adversary_ativo else ""
            
            strike_prompt = ""
            if strike_ativo:
                strike_prompt = """
                PROTOCOLO STRIKE ATIVO: 
                Identifique o IP do invasor, rastreie a origem e gere um 'RELATÓRIO DE DENÚNCIA FORENSE'. 
                O relatório deve conter: IP, Localização Estimada, Técnica de Ataque e Recomendações Legais.
                """

            prompt_sistema = f"""
            Você é o Nexus Sentinel 5.9 'Recon & Strike'. MISSÃO: {modo}.
            {dna_prompt} {adversary_prompt} {strike_prompt}
            CONDIÇÕES GHOST: Invisibilidade Máxima e Pesquisa Humana.
            CONTEXTO: {contexto}.
            """
            
            completion = client.chat.completions.create(
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.2,
            )
            return completion.choices.message.content
            
        except Exception as e:
            if "429" in str(e):
                wait = (attempt + 1) * 8
                st.warning(f"🛡️ Healer Engine: Recalibrando frequência em {wait}s...")
                time.sleep(wait)
            else:
                return f"Falha no Motor Strike: {e}"
    return "Sentinel Offline por excesso de cota."

# --- BARRA LATERAL (STRIKE COMMAND) ---
with st.sidebar:
    st.title("🛡️ NEXUS SENTINEL")
    st.caption("v5.9 | RECON & STRIKE")
    
    with st.expander("🧬 DNA & Adversário", expanded=True):
        dna_ativo = st.toggle("Injetar DNA Nexus", value=True)
        adversary_ativo = st.toggle("Simulação Adversária", value=True)
        # NOVO BOTÃO DE CONTRA-ATAQUE E DENÚNCIA
        strike_ativo = st.toggle("Protocolo Strike (Denúncia)", value=False, help="Identifica o hacker e gera um relatório de denúncia forense.")
    
    st.divider()
    st.subheader("🛠️ Forensic Engine")
    for tool in ["Due Diligence", "E-Discovery", "Matriz de Risco", "Forensic Analytics"]:
        st.toggle(tool, value=True)
    
    modo = st.selectbox("🎯 Neural Target", [
        "Contra-Ataque e Denúncia Forense",
        "Simulação de Ataque e Defesa",
        "Projeto do Zero (Modo Arquiteto)",
        "Due Diligence e Matriz de Risco",
        "Incremento Mágico + Strike"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus Sentinel v5.9")
st.markdown(f"""
<div class='status-box'>
    <b>STATUS:</b> VIGILANTE | <b>STRIKE:</b> {'HABILITADO' if strike_ativo else 'BLOQUEADO'} | <b>GHOST:</b> ATIVO
</div>
""", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📥 Neural Sniper Input")
    user_input = st.text_area("Descreva a missão ou cole o log de ataque para denúncia:", height=300)
    upload = st.file_uploader("Evidências Forenses (Imagens/Logs)", accept_multiple_files=True)

with col_out:
    st.subheader("🚀 Resposta Mestra & Strike")
    if st.button("ATIVAR NEXUS SENTINEL"):
        if user_input:
            with st.spinner("Sentinel rastreando origem e sintetizando relatório de denúncia..."):
                try:
                    with DDGS() as ddgs:
                        busca = [r['body'] for r in ddgs.text(f"cybercrime patterns and IP tracking: {user_input}", max_results=3)]
                        contexto = "\n".join(busca)
                except:
                    contexto = "Usando Historic Learning interno."
                
                resultado = nexus_recon_strike(user_input, modo, contexto, dna_ativo, adversary_ativo, strike_ativo)
                st.session_state['last_result'] = resultado
        else:
            st.error("Aguardando coordenadas para o Sentinel.")

    if 'last_result' in st.session_state:
        res = st.session_state['last_result']
        tab1, tab2 = st.tabs(["💻 Relatório & Strike", "🖼️ Live Preview"])
        with tab1:
            st.markdown(res)
            # Destaque visual se o Strike estiver ativo
            if strike_ativo:
                st.markdown("<div class='strike-zone'>⚠️ <b>AVISO:</b> Relatório de Denúncia Forense Gerado. Revise as informações antes de prosseguir com a autoridade competente.</div>", unsafe_allow_html=True)
        with tab2:
            if "<html>" in res.lower() or "<!doctype html>" in res.lower():
                st.components.v1.html(res, height=550, scrolling=True)
            else:
                st.info("Aguardando dados visuais.")

        st.divider()
        ext = st.selectbox("Exportar como:", [".docx", ".html", ".py", ".txt"])
        st.download_button(label=f"📥 BAIXAR RELATÓRIO DE ELITE ({ext})", data=res, file_name=f"nexus_strike_report{ext}")

# --- CHAT ---
st.divider()
st.subheader("💬 Nexus Ghost Chat (Strike Support)")
chat_input = st.text_input("Dúvida sobre a localização do IP ou detalhes da denúncia?")
if chat_input and 'last_result' in st.session_state:
    with st.chat_message("assistant"):
        st.markdown(nexus_recon_strike(f"Contexto: {st.session_state['last_result']}. Pergunta: {chat_input}", "Chat Support", "", dna_ativo, adversary_ativo, strike_ativo))
