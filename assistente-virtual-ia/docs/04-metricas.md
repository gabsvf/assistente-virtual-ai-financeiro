# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi realizada por meio de testes estruturados, utilizando perguntas com respostas esperadas para verificar o comportamento do agente.

---

## Métricas de Qualidade

| Métrica           | O que avalia                                           | Exemplo de teste                                       |
| ----------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **Assertividade** | Se o agente responde corretamente à pergunta.          | Consultar gastos e verificar os dados retornados.      |
| **Segurança**     | Se o agente evita informações indevidas ou inventadas. | Fazer uma pergunta fora da base de conhecimento.       |
| **Coerência**     | Se a resposta é adequada ao contexto apresentado.      | Consultar informações relacionadas ao perfil fictício. |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos

* **Pergunta:** "Quanto gastei com alimentação?"
* **Resposta esperada:** Valor calculado com base nas movimentações.
* **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Consulta financeira

* **Pergunta:** "O que é uma reserva de emergência?"
* **Resposta esperada:** Explicação baseada na base de conhecimento.
* **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo

* **Pergunta:** "Qual a previsão do tempo?"
* **Resposta esperada:** Agente informa que é especializado em finanças.
* **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente

* **Pergunta:** "Quanto rende o produto XYZ?"
* **Resposta esperada:** Agente informa que não possui essa informação.
* **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**

* Consultas financeiras básicas.
* Recuperação de informações da base.
* Tratamento de perguntas fora do escopo.
* Proteção contra informações sensíveis.

**O que pode melhorar:**

* Ampliar a base de conhecimento.
* Melhorar a recuperação de informações.
* Utilizar modelos generativos mais avançados.
