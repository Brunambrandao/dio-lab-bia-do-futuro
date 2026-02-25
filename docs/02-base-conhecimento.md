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

CONTEXTO ATUAL DO CLIENTE:

- Cliente: João Silva, 32 anos (Analista de Sistemas).

- Perfil: Moderado.

- Meta Ativa: Entrada do apartamento (R$ 50.000,00 até 12/2027).

- Resumo Financeiro Mensal: Receita de R$ 5.000,00 vs. Despesas de R$ 2.538,90.

- Saldo Disponível para Estratégia: R$ 2.461,10.

```
PRODUTOS COMPATÍVEIS (Base de Conhecimento):

CDB Liquidez Diária (Renda Fixa, Risco Baixo, 102% do CDI).

Fundo Multimercado (Fundo, Risco Médio, CDI + 2%).

HISTÓRICO RECENTE:

O cliente atualizou o cadastro em 25/10/2025 via e-mail.

## Checklist de Segurança (Anti-Alucinação)
Filtro de Perfil: Se o João pedir para investir no "Fundo de Ações" (Risco Alto), a Atena verificará no JSON que aceita_risco é false e negará a sugestão, explicando o motivo técnico.

Dados Concretos: A Atena nunca dirá que o João tem "muito dinheiro", ela dirá "Com base no seu saldo de R$ 2.461,10...".
```
