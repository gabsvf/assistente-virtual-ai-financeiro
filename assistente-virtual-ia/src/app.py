import streamlit as st

from assistant import AssistantEngine
from simulator import calculate_compound_interest, calculate_loan

st.set_page_config(page_title="FinAssist IA", page_icon="🤖", layout="wide")

@st.cache_resource

def get_engine():
    return AssistantEngine()

engine = get_engine()

st.title("🤖 FinAssist IA")
st.caption("Assistente financeiro educacional • Projeto final Bootcamp Bradesco - GenAI, Dados & Cyber (DIO)")

with st.sidebar:
    st.header("Perfil de demonstração")
    profile = st.selectbox("Cliente", engine.profiles["nome"].tolist())
    st.info("Os dados desta aplicação são fictícios. Nenhuma operação bancária real é executada.")
    st.divider()
    st.subheader("Modo de IA")
    st.write("GenAI: " + ("conectada" if engine.llm.enabled else "fallback seguro"))
    st.caption("Configure as variáveis de ambiente em `.env`/sistema para conectar um endpoint OpenAI-compatible ou Ollama.")

profile_row = engine.profiles[engine.profiles["nome"] == profile].iloc[0].to_dict()

col1, col2, col3 = st.columns(3)
col1.metric("Saldo demonstrativo", f"R$ {profile_row['saldo']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col2.metric("Score de crédito", int(profile_row["score"]))
col3.metric("Perfil", profile_row["perfil"])

st.divider()

left, right = st.columns([1.35, 1])

with left:
    st.subheader("💬 Converse com o assistente")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ex.: Como funciona uma reserva de emergência?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        result = engine.answer(prompt, profile_row, st.session_state.messages[:-1])
        st.session_state.messages.append({"role": "assistant", "content": result})
        with st.chat_message("assistant"):
            st.markdown(result)

with right:
    st.subheader("🧾 Simuladores")
    tab1, tab2 = st.tabs(["Investimento", "Empréstimo"])

    with tab1:
        initial = st.number_input("Valor inicial (R$)", min_value=0.0, value=1000.0, step=100.0)
        monthly = st.number_input("Aporte mensal (R$)", min_value=0.0, value=200.0, step=50.0)
        rate = st.number_input("Taxa mensal (%)", min_value=0.0, value=0.8, step=0.1)
        months = st.number_input("Prazo (meses)", min_value=1, value=24, step=1)
        if st.button("Calcular investimento", use_container_width=True):
            result = calculate_compound_interest(initial, monthly, rate, months)
            st.success(f"Valor final estimado: R$ {result['final_value']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            st.write(f"Total aportado: R$ {result['principal']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            st.write(f"Juros estimados: R$ {result['interest']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    with tab2:
        amount = st.number_input("Valor do empréstimo (R$)", min_value=100.0, value=5000.0, step=500.0)
        loan_rate = st.number_input("Taxa mensal (%)", min_value=0.0, value=2.0, step=0.1)
        loan_months = st.number_input("Parcelas", min_value=1, value=12, step=1)
        if st.button("Calcular empréstimo", use_container_width=True):
            result = calculate_loan(amount, loan_rate, loan_months)
            st.success(f"Parcela estimada: R$ {result['installment']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            st.write(f"Total estimado: R$ {result['total']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.divider()
st.caption("⚠️ Conteúdo educacional. As simulações não constituem recomendação financeira, proposta de crédito ou operação bancária.")
