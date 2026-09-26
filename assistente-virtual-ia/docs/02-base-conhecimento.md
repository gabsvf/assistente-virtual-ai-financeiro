# Base de Conhecimento

## Dados Utilizados

| Arquivo                         | Formato | Utilização no Agente                                   |
| ------------------------------- | ------- | ------------------------------------------------------ |
| `faq_financeiro.csv`            | CSV     | Perguntas e respostas sobre conceitos financeiros.     |
| `produtos_financeiros.csv`      | CSV     | Informações demonstrativas sobre produtos financeiros. |
| `clientes_demo.csv`             | CSV     | Perfis financeiros fictícios para contextualização.    |
| `movimentacoes_financeiras.csv` | CSV     | Receitas e despesas fictícias para análise financeira. |

> Todos os dados de clientes e movimentações são fictícios e utilizados apenas para demonstração.

---

## Adaptações nos Dados

Os dados foram expandidos com mais registros, datas recentes, valores variados e novas categorias de receitas e despesas, como moradia, alimentação, transporte, saúde, lazer, educação, compras e serviços.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos CSV da pasta `data/` são carregados pela aplicação Python durante sua execução.

### Como os dados são usados no prompt?

Os dados são consultados de forma dinâmica. A pergunta do usuário é analisada, registros relevantes são recuperados e essas informações são adicionadas ao contexto enviado ao modelo de IA.

---

## Exemplo de Contexto Montado

```text
Perfil:
- Nome: Cliente Demo
- Perfil: Moderado

Movimentações:
- 2026-09-03: Supermercado - R$ 382,40
- 2026-09-10: Uber - R$ 32,70
- 2026-09-15: Farmácia - R$ 76,90

Conhecimento:
- Reserva de emergência: valor destinado a despesas inesperadas.
- CDI: taxa de referência utilizada no mercado financeiro brasileiro.

Instrução:
Responder utilizando os dados disponíveis e não inventar informações.
```
