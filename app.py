import streamlit as st
import pandas as pd
from groq import Groq
from duckduckgo_search import DDGS

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Nexus OmniCode", page_icon="⚡", layout="wide")

# --- ESTILO CSS PARA DESIGN BONITO ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4CAF50; color: white; }
    .stTextInput>div>div>input { color: #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE BLINDAGEM (SENHA) ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    senha = st.text_input("Digite a chave mestra para acessar o Nexus OmniCode:", type="password")
    if senha == "admin123": # Altere sua senha aqui
        st.session_state['autenticado'] = True
        st.rerun()
    else:
        st.warning("Sistema Blindado. Aguardando chave...")
        st.stop()

# --- SIDEBAR (FILTROS E INTEGRAÇÕES) ---
st.sidebar.title("🔗 Integrações Nexus")
sistemas = ["GitLab", "Bitbucket", "Azure DevOps", "Gitea", "SourceForge", "FastAPI"]
for s in sistemas:
    st.sidebar.toggle(f"Conectar {s}", value=True)

st.sidebar.divider()
st.sidebar.title("🛠️ Ferramentas")
funcao = st.sidebar.selectbox("O que deseja fazer?", ["Criar Código do Zero", "Corrigir Erros", "Analisar Performance", "Aprimorar Código Existente"])

# --- FUNÇÃO DE PESQUISA "INVISÍVEL" (Simula consulta humana) ---
def buscar_conhecimento_ia(pergunta):
    with DDGS() as ddgs:
        resultados = [r['body'] for r in ddgs.text(f"melhor solução de código para: {pergunta}", max_results=3)]
    return "\n".join(resultados)

# --- CORPO PRINCIPAL ---
st.title("⚡ Nexus OmniCode")
st.subheader("O Analista Universal de Códigos")

col1, col2 = st.columns([2, 1])

with col1:
    ideia = st.text_area("Descreva sua ideia ou cole seu código aqui:", height=200, placeholder="Ex: Crie um sistema de login com banco de dados...")
    arquivo_upload = st.file_uploader("Upload de arquivo para análise", type=['py', 'js', 'html', 'css', 'txt'])

with col2:
    st.info("O Nexus está consultando múltiplas fontes agora para garantir o melhor resultado.")
    if st.button("🚀 EXECUTAR NEXUS"):
        if ideia:
            with st.spinner("Nexus consultando IAs mundiais e sintetizando resposta..."):
                # Simulação de consulta e análise
                contexto_externo = buscar_conhecimento_ia(ideia)
                
                # Aqui você conectaria sua API KEY da Groq (Grátis)
                # Por enquanto, geramos uma resposta simulada de alta qualidade
                resposta_final = f"### ✅ Código Otimizado pelo Nexus\n\n```python\n# Baseado em análises de múltiplas IAs\n# Função: {funcao}\n\ndef nexus_optimized_solution():\n    # Código simulado de alta performance\n    print('Nexus analisou GitLab e Azure para esta solução')\n    return True\n```\n\n**Análise de Melhorias:**\n- Removido redundâncias encontradas no Bitbucket.\n- Aplicado padrão SecOps do GitLab."
                
                st.success("Análise Concluída!")
                st.markdown(resposta_final)
                
                # Botão de Download
                st.download_button("📥 Baixar Código Gerado", resposta_final, file_name="nexus_code.py")
        else:
            st.error("Por favor, digite uma ideia ou código.")

# --- BIBLIOTECA DE COMANDOS (COPIE E COLE) ---
st.divider()
with st.expander("📚 Biblioteca de Prompts Nexus (Copie e Cole)"):
    st.code("Nexus, analise este código e aplique padrões de segurança do GitLab SecOps.")
    st.code("Nexus, crie um script Python que automatize o upload para Bitbucket via API.")
    st.code("Nexus, encontre erros de lógica neste código e gere a versão aprimorada.")
