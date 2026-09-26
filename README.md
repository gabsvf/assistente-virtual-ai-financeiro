# FinAssist IA

Projeto final do **Bootcamp Bradesco - GenAI, Dados & Cyber (DIO)**.

O FinAssist IA é um assistente virtual financeiro criado para responder dúvidas, consultar dados financeiros fictícios e realizar simulações.

## Objetivo

Demonstrar o uso de **Inteligência Artificial, Python, dados e segurança** em uma aplicação financeira simples.

## Funcionalidades

* Chat com perguntas financeiras.
* Consulta a uma base de conhecimento em CSV.
* Integração opcional com IA generativa.
* Simulador de investimentos e empréstimos.
* Dados fictícios de clientes e movimentações.
* Proteção contra dados sensíveis.
* Detecção básica de prompt injection.

## Estrutura

```text
assistente-virtual-ia/
├── data/
├── docs/
└── src/
```

## Tecnologias

* Python
* Streamlit
* Pandas
* IA Generativa
* CSV
* Git/GitHub

## Como executar

```bash
cd assistente-virtual-ia
python -m venv .venv
.venv\Scripts\activate
```

```bash
pip install -r src/requirements.txt
```

```bash
streamlit run src/app.py
```

## Observação

O projeto é **educacional**, utiliza dados fictícios e não realiza operações bancárias reais.
