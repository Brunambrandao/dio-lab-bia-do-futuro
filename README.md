# 🤖 Atena: Assistente Financeira Inteligente

A **Atena** é uma assistente de inteligência financeira proativa, desenvolvida para transformar dados bancários brutos em decisões seguras e inteligentes. Este projeto utiliza IA Generativa para oferecer consultoria personalizada, garantindo **segurança, ética e educação financeira** em cada interação.

---

## 🎯 Caso de Uso
O projeto resolve a dificuldade de interpretação de dados financeiros complexos. A Atena atua como uma consultora consultiva que:
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
## 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologia |
|-----------|------------|
| **LLM** | Google Gemini 1.5 Flash |
| **Interface** | Streamlit |
| **Linguagem** | Python 3.10+ |
| **Biblioteca de Dados** | Pandas |
| **Configuração** | Python-dotenv |

---

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---


📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

📁 **Pasta:** [`src/`](./src/)

---


📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---


📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md                # Apresentação do projeto
│
├── 📁 data/                    # Base de Conhecimento
│   ├── perfil_investidor.json  # Perfil do cliente João Silva
│   └── transacoes.csv          # Histórico real de transações
│
├── 📁 docs/                    # Documentação Técnica
│   ├── 01-documentacao-agente.md
│   ├── 03-prompts.md           # System Prompts e Personas
│   └── 04-metricas.md          # Relatório de Assertividade e Segurança
│
├── 📁 src/                     # Código Fonte
│   ├── app.py                  # Interface Streamlit (Chat)
│   ├── agente.py               # Lógica de processamento de dados
│   └── requirements.txt        # Dependências do projeto
│
└── 📁 assets/                  # Evidências e capturas de tela
```

---
