# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Evitar repetição de explicações (ex: Atena sabe que o João já perguntou sobre CDB em 15/09). |
| `perfil_investidor.json` | JSON | Identificar que o João é "Moderado" e tem como meta a "Entrada do Apartamento". |
| `produtos_financeiros.json` | JSON | Filtrar apenas produtos que se encaixam no perfil "Moderado" ou "Baixo" do João. |
| `transacoes.csv` | CSV | Calcular o saldo real e identificar que o Salário (R$ 5.000) já caiu na conta. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? 

A Atena não lerá apenas os dados estáticos, ela somará as entradas e subtrairá as saídas do transacoes.csv para dizer ao João exatamente quanto "sobrou" para investir no mês.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos são carregados via biblioteca Pandas no Python assim que a aplicação Streamlit inicia. Eles ficam armazenados em dataframes na memória da sessão.

### Como os dados são usados no prompt?

Utilizaremos a técnica de Dynamic Context Injection (Injeção Dinâmica de Contexto). Em vez de jogar todo o banco de dados no prompt (o que seria caro e confuso), a Atena:

1- Identifica a intenção do usuário.

2-  Filtra apenas as linhas relevantes (ex: se o usuário quer investir, ela puxa apenas o perfil_investidor.json e os produtos compatíveis do produtos_financeiros.json).

3- Insere esses dados formatados como texto no System Prompt.

---

## Exemplo de Contexto Montado

Para garantir que não haja alucinação, o contexto será enviado assim para o modelo:

```
CONTEXTO ATUAL DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Metas: Completar reserva (R$ 15k) e Entrada apto (R$ 50k)
- Saldo Calculado: R$ 2.461,10 (Baseado em transacoes.csv)

PRODUTOS COMPATÍVEIS:
- CDB Liquidez Diária: Risco Baixo, 102% do CDI
- Fundo Multimercado: Risco Médio, CDI + 2%

HISTÓRICO:
- 25/10/2025: Atualização cadastral via email
```
---
## Nota de Segurança (Anti-Alucinação):

O sistema de filtragem impede que produtos de "Risco Alto" (como o Fundo de Ações) sejam injetados no contexto acima, pois o campo aceita_risco do cliente é false.
