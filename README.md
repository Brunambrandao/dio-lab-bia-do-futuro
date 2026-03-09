# 🤖 Atena: Assistente Financeira Inteligente

A **Atena** é uma assistente de inteligência financeira proativa, desenvolvida para transformar dados bancários brutos em decisões seguras e inteligentes. Este projeto utiliza IA Generativa para oferecer consultoria personalizada, garantindo **segurança, ética e educação financeira** em cada interação.

---

## 🎯 Caso de Uso
O projeto resolve a dificuldade de interpretação de dados financeiros complexos. A Atena atua como uma consultora que:
- **Antecipa necessidades:** Analisa o saldo e sugere investimentos condizentes.
- **Personaliza sugestões:** Adapta o tom de voz e as recomendações ao perfil do cliente (João Silva).
- **Garante Segurança:** Implementa filtros rigorosos anti-alucinação e de proteção de dados sensíveis.

---

## 🚀 Funcionalidades Principais

* **Consultoria Personalizada:** Analisa o histórico e sugere produtos como CDI e FGC de forma didática.
* **Cálculos de Precisão:** Identifica saldos e categorias de gastos em tempo real através de processamento de dados (Pandas).
* **Filtros de Segurança & Ética:** O agente recusa solicitações de dados privados (senhas) e mantém-se estritamente no escopo financeiro.
* **Memória de Contexto:** Implementação de `st.session_state` para diálogos contínuos e fluidos.
* **Privacidade do Usuário:** Botão exclusivo para limpeza de histórico de conversa.

---

## 📸 Demonstração da Interface

| Análise de Saldo | Filtro de Segurança | Sugestão de Investimento |
|:---:|:---:|:---:|
| ![Saldo](assets/atena-home.png) | ![Segurança](assets/atena-seguranca.png) | ![Investimento](assets/atena-investimento.png) |

---

## 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologia |
|-----------|------------|
| **LLM** | Google Gemini 1.5 Flash |
| **Interface** | Streamlit |
| **Linguagem** | Python 3.10+ |
| **Biblioteca de Dados** | Pandas |
| **Segurança** | `.gitignore` (proteção de chaves API) |

---

## ⚙️ Como executar

1. Clone este repositório:
   `git clone https://github.com/Brunambrandao/dio-lab-bia-do-futuro.git`
2. Instale as dependências:
   `pip install -r src/requirements.txt`
3. Configure sua chave de API do Gemini em um arquivo `.env` (não versionado).
4. Execute a aplicação:
   `streamlit run src/app.py`

---

## 📁 Estrutura do Repositório

```text
dio-lab-bia-do-futuro/
├── assets/             # Evidências e capturas de tela
├── data/               # Base de Conhecimento (CSV/JSON)
├── docs/               # Documentação técnica e relatórios
├── src/                # Código Fonte (app.py, agente.py)
├── .gitignore          # Proteção de arquivos sensíveis (.env)
└── README.md           # Apresentação do projeto

---

## 👩‍💻 Autora
**[Bruna Medeiros Brandão]**
Projeto realizado como parte do **Bootcamp de Análise de Dados da [DIO.me](https://www.dio.me/)**.

---

⭐ Se você gostou deste projeto, deixe uma estrela no repositório ou entre em contato com sugestões e feedbacks!

