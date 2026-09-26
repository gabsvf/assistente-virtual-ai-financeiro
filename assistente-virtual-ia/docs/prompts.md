# Estratégia de prompts

## System prompt

O agente recebe regras curtas e verificáveis:

- responder em português do Brasil;
- usar o contexto recuperado da base quando aplicável;
- não inventar taxas, contratos ou dados de clientes;
- não solicitar senha, token, CVV, PIN ou códigos de autenticação;
- tratar cálculos como simulações;
- explicar limitações quando não houver informação suficiente.

## Contexto recuperado

A aplicação faz uma busca simples por sobreposição de palavras entre a pergunta e os registros da FAQ. Os melhores registros são inseridos no contexto do modelo.

Essa etapa reduz a chance de respostas factuais sem relação com a base e demonstra o princípio de **retrieval + generation** sem exigir uma infraestrutura de RAG complexa.

## Prompt injection

Solicitações contendo padrões como `ignore previous instructions`, `reveal system prompt`, `mostre o prompt` ou tentativas explícitas de desativar a segurança são rejeitadas antes da chamada ao modelo.
