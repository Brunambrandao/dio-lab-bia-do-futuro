import streamlit as st
import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

sys.path.append(os.path.dirname(__file__))
from agente import carregar_dados_joao

st.set_page_config(page_title="Atena - IA Financeira", page_icon="🤖")

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Erro: Chave não encontrada.")
else:
    genai.configure(api_key=api_key)
    st.title("🤖 Atena: Sua Assistente de Investimentos")

    # --- BARRA LATERAL COM BOTÃO DE LIMPAR ---
    with st.sidebar:
        st.header("Configurações")
        if st.button("🗑️ Limpar Conversa"):
            st.session_state.historico = []
            st.rerun() # Faz a página recarregar e limpar a tela

    # --- INICIALIZAÇÃO DA MEMÓRIA ---
    if "historico" not in st.session_state:
        st.session_state.historico = []

    transacoes, perfil = carregar_dados_joao()

    if transacoes is not None:
        st.success(f"Conectada ao perfil de: {perfil['nome']}")

        # Exibe o histórico de mensagens
        for mensagem in st.session_state.historico:
            with st.chat_message(mensagem["role"]):
                st.write(mensagem["content"])

        # Campo de pergunta (rodapé)
        if pergunta := st.chat_input("Como posso ajudar com seus investimentos hoje?"):
            
            st.session_state.historico.append({"role": "user", "content": pergunta})
            with st.chat_message("user"):
                st.write(pergunta)

            with st.chat_message("assistant"):
                with st.spinner('Atena analisando...'):
                    try:
                        modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                        escolhido = "models/gemini-1.5-flash" if "models/gemini-1.5-flash" in modelos else modelos[0]
                        model = genai.GenerativeModel(escolhido)

                        historico_texto = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.historico])
                        contexto = f"Você é a Atena. Dados: {perfil}. Histórico: {transacoes.to_string()}\n\nConversa anterior:\n{historico_texto}"
                        
                        response = model.generate_content(f"{contexto}\n\nPergunta atual: {pergunta}")
                        
                        resposta_atena = response.text
                        st.write(resposta_atena)
                        st.session_state.historico.append({"role": "assistant", "content": resposta_atena})
                        
                    except Exception as e:
                        st.error(f"Erro: {e}")