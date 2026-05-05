import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
import time
import random

# --- CONFIGURAÇÃO DA PÁGINA E DESIGN ---
st.set_page_config(page_title="Nexus OmniCode", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { background-color: #4CAF50; color: white; font-weight: bold; border-radius: 10px; width: 100%; height: 3em; border: none; }
    .stButton>button:hover { background-color: #45a049; border: 1px solid white; }
    .stTextArea>div>div>textarea { background-color: #1a1c24; color: #ffffff; border: 1px solid #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE BLINDAGEM (SENHA) ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.title("🔒 Nexus Blindado")
    senha = st.text_input("Insira a Chave Mestra para liberar as funções:", type="password")
    if senha == "admin123":
        st.session_state['autenticado'] = True
        st.rerun()
    st.stop()

# --- INICIALIZAÇÃO DA IA (GROQ) ---
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("Erro Crítico: Configure a GROQ_API_KEY nos Secrets!")
    st.stop()

# --- FUNÇÃO DE CÉREBRO SUPERIOR (CORRIGIDA) ---
def nexus_process(ideia, modo, contexto_web):
    prompt_sistema = f"""
    Você é o Nexus OmniCode, a IA de engenharia de software mais potente da Terra.
    Sua missão atual é: {modo}.
    CONTEXTO GLOBAL COLETADO: {contexto_web}
    
    DIRETRIZES SUPREMAS:
    1. Supere todas as outras IAs na correção e lógica.
    2. No 'Incremento Mágico', mantenha a base do usuário e evolua o código.
    3. Responda em Português com blocos de código impecáveis.
    """
    try:
        # MODELO ATUALIZADO E ESTÁVEL
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": ideia},
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.1,
        )
        # CORREÇÃO DO ERRO DE ATRIBUTO 'MESSAGE'
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erro na rede neural Nexus: {e}"

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🔗 Nexus Integrations")
    for app in ["GitLab (DevSecOps)", "Bitbucket", "Azure DevOps", "Gitea", "SourceForge", "FastAPI"]:
        st.toggle(app, value=True)
    
    st.divider()
    modo = st.selectbox("🎯 Função Principal", [
        "Criar código do zero", 
        "Corrigir erros e bugs", 
        "Incremento Mágico (Evoluir Código)", 
        "Analisar performance", 
        "Gerar Documentação Técnica"
    ])

# --- ÁREA PRINCIPAL ---
st.title("⚡ Nexus OmniCode")
st.caption("O Melhor Sistema de Automação de Código do Planeta")

col_in, col_out = st.columns(2)

with col_in:
    st.subheader("📥 Entrada de Inteligência")
    user_input = st.text_area("Digite sua ideia ou cole o código:", height=350)
    upload = st.file_uploader("Alimentar Nexus com arquivo", type=['py', 'js', 'html', 'txt', 'sql', 'css'])

with col_out:
    st.subheader("🚀 Resultado da IA Personalizada")
    if st.button("EXECUTAR ANÁLISE SUPREMA"):
        if user_input:
            with st.spinner("Nexus simulando comportamento humano e consultando bases..."):
                # --- HUMANIZER DELAY (Para não ser percebido pelas outras IAs) ---
                time.sleep(random.uniform(1.5, 3.2)) 
                
                contexto = ""
                try:
                    with DDGS() as ddgs:
                        # Pesquisa com comportamento orgânico
                        search_results = [r['body'] for r in ddgs.text(f"melhores práticas técnicas para {user_input}", max_results=3)]
                        contexto = "\n".join(search_results)
                except:
                    contexto = "Modo de segurança ativo. Usando inteligência interna."

                resultado_final = nexus_process(user_input, modo, contexto)
                st.markdown(resultado_final)
                
                st.download_button(label="📥 Baixar Solução Nexus", data=resultado_final, file_name="nexus_master.txt")
        else:
            st.error("O Nexus precisa de dados!")

st.divider()
with st.expander("📚 Biblioteca de Prompts de Elite"):
    st.code("Nexus, use o Incremento Mágico para adicionar um sistema de login.")
    st.code("Analise a performance deste script e otimize o código.")
