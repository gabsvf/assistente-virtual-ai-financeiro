# Arquitetura

```text
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    └──────────┬───────────┘
                               │
                       mensagem do usuário
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Camada de segurança │
                    │ sanitização + regras │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Recuperação de dados │
                    │ FAQ + perfil fictício│
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ LLM opcional    │        │ Fallback local  │
        │ OpenAI-compatible│       │ regras + FAQ    │
        └────────┬────────┘        └────────┬────────┘
                 └─────────────┬─────────────┘
                               ▼
                      resposta ao usuário
```

## Decisões

**Dados:** CSV foi escolhido para manter o projeto transparente, pequeno e fácil de reproduzir em um bootcamp.

**IA:** a camada generativa é opcional. Assim, a avaliação do projeto não depende de uma chave de API ou de um provedor específico.

**Segurança:** a entrada do usuário passa por sanitização antes de chegar ao modelo. O assistente também possui regras para não solicitar credenciais e para rejeitar tentativas explícitas de alterar suas instruções internas.

**Privacidade:** os perfis são fictícios e a aplicação não possui integração com banco real.
