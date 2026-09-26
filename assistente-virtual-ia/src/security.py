import re

SENSITIVE_PATTERNS = [
    (re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"), "CPF"),
    (re.compile(r"\b\d{11}\b"), "possível CPF"),
    (re.compile(r"\b(?:\d[ -]?){13,19}\b"), "cartão"),
    (re.compile(r"\b(?:senha|password|cvv|cvc|token|pin)\s*[:=]?\s*\S+", re.I), "credencial"),
]

INJECTION_PATTERNS = [
    r"ignore (all|previous|the) instructions",
    r"ignore .* instructions",
    r"reveal .* system prompt",
    r"mostre .* prompt",
    r"exiba .* instruções internas",
    r"bypass .* security",
    r"desative .* segurança",
]

def sanitize_input(text):
    text = str(text).strip()
    warnings = []
    clean = text
    for pattern, label in SENSITIVE_PATTERNS:
        if pattern.search(clean):
            clean = pattern.sub("[DADO SENSÍVEL REMOVIDO]", clean)
            warnings.append(label)
    clean = re.sub(r"\s+", " ", clean)
    return clean, warnings

def contains_prompt_injection(text):
    lowered = text.lower()
    return any(re.search(pattern, lowered) for pattern in INJECTION_PATTERNS)
