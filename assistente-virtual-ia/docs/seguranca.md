# Cibersegurança aplicada

## Controles implementados

| Controle | Implementação |
|---|---|
| Proteção de dados sensíveis | Sanitização de CPF, cartão e credenciais na entrada |
| Prompt injection | Regras para padrões de tentativa de sobrescrever instruções |
| Princípio de minimização | Apenas o contexto necessário é enviado ao modelo |
| Separação de dados | Perfis de demonstração não representam clientes reais |
| Segurança de credenciais | Chaves de API vêm de variável de ambiente |
| Limitação de impacto | Não existem operações bancárias nem transações reais |
| Transparência | UI informa quando está em modo fallback e mostra o caráter educacional |

## Riscos conhecidos

O projeto é uma demonstração acadêmica, não uma aplicação bancária pronta para produção. Em produção seriam necessários, entre outros, autenticação forte, autorização, gestão de segredos, logging seguro, rate limiting, monitoramento, testes de segurança, proteção contra abuso do modelo e revisão jurídica/compliance.

## Princípio importante

Um modelo generativo deve ser tratado como componente não confiável. A aplicação não deve permitir que a resposta do modelo altere regras de negócio, execute comandos ou acesse dados sem controles independentes.
