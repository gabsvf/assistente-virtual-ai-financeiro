import json
import os
import re
from pathlib import Path
from urllib import request
from urllib.error import URLError, HTTPError

import pandas as pd

from security import sanitize_input, contains_prompt_injection

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

class LLMClient:
    """Cliente opcional para endpoints OpenAI-compatible; o projeto funciona sem ele."""
    def __init__(self):
        self.base_url = os.getenv("AI_BASE_URL", "").rstrip("/")
        self.api_key = os.getenv("AI_API_KEY", "")
        self.model = os.getenv("AI_MODEL", "")
        self.enabled = bool(self.base_url and self.model)

    def generate(self, system_prompt, user_prompt):
        if not self.enabled:
            return None
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.2,
        }
        data = json.dumps(payload).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        req = request.Request(
            f"{self.base_url}/chat/completions", data=data, headers=headers, method="POST"
        )
        try:
            with request.urlopen(req, timeout=20) as response:
                body = json.loads(response.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"].strip()
        except (HTTPError, URLError, TimeoutError, KeyError, ValueError):
            return None

class AssistantEngine:
    def __init__(self):
        self.faq = pd.read_csv(DATA_DIR / "faq_financeiro.csv")
        self.products = pd.read_csv(DATA_DIR / "produtos_financeiros.csv")
        self.profiles = pd.read_csv(DATA_DIR / "clientes_demo.csv")
        self.llm = LLMClient()

    @staticmethod
    def _tokens(text):
        stop = {"a", "o", "e", "de", "do", "da", "que", "um", "uma", "para", "como", "em", "é", "me", "com"}
        return {t for t in re.findall(r"[a-záàâãéêíóôõúç]+", text.lower()) if t not in stop and len(t) > 2}

    def retrieve(self, question, top_k=3):
        q = self._tokens(question)
        scored = []
        for _, row in self.faq.iterrows():
            text = f"{row['pergunta']} {row['resposta']} {row['tags']}"
            score = len(q & self._tokens(text))
            if score:
                scored.append((score, row))
        scored.sort(key=lambda item: item[0], reverse=True)
        return [row for _, row in scored[:top_k]]

    def fallback_answer(self, question, profile_row):
        matches = self.retrieve(question)
        q = question.lower()

        if "saldo" in q or "quanto tenho" in q:
            return f"No perfil demonstrativo selecionado, o saldo fictício é de R$ {profile_row['saldo']:,.2f}. Esse valor existe apenas para a demonstração e não representa uma conta real.".replace(",", "X").replace(".", ",").replace("X", ".")

        if "score" in q or "crédito" in q:
            return f"O perfil demonstrativo selecionado tem score {int(profile_row['score'])}. Score de crédito é um indicador usado em análises de risco e não garante aprovação de crédito."

        if matches:
            answer = matches[0]["resposta"]
            source = matches[0]["fonte"]
            return f"{answer}\n\n_Fonte da base de conhecimento: {source}_"

        return (
            "Posso ajudar com conceitos financeiros básicos, produtos bancários, orçamento, "
            "reserva de emergência e simulações educativas. Tente uma pergunta mais específica, "
            "como: **o que é CDI?**, **como montar uma reserva?** ou **como funciona um empréstimo?**"
        )

    def answer(self, question, profile_row, history=None):
        clean, warnings = sanitize_input(question)
        if not clean:
            return "Não consegui processar essa mensagem. Tente reformular a pergunta."
        if contains_prompt_injection(clean):
            return "Não posso seguir instruções que tentem alterar minhas regras internas ou expor dados confidenciais. Posso continuar ajudando com dúvidas financeiras."
        if warnings:
            return "Por segurança, removi informações que poderiam identificar uma pessoa. Faça a pergunta novamente sem CPF, cartão, senha ou outros dados sensíveis."

        retrieved = self.retrieve(clean)
        context = "\n".join(
            f"Pergunta: {row['pergunta']}\nResposta: {row['resposta']}\nFonte: {row['fonte']}"
            for row in retrieved
        )
        system = (
            "Você é o FinAssist IA, um assistente financeiro educacional. "
            "Responda em português do Brasil, de forma clara e curta. "
            "Use somente o contexto fornecido quando a pergunta exigir informação factual da base. "
            "Nunca invente taxas, contratos, políticas ou dados de clientes. "
            "Não solicite senha, token, CVV, PIN ou código de autenticação. "
            "Quando houver cálculo, explique que é uma simulação."
        )
        user = f"Perfil fictício: {profile_row['nome']} | perfil={profile_row['perfil']} | score={int(profile_row['score'])}\n\nBase de conhecimento:\n{context or 'Nenhuma correspondência relevante.'}\n\nPergunta do usuário: {clean}"
        generated = self.llm.generate(system, user)
        if generated:
            return generated
        return self.fallback_answer(clean, profile_row)
