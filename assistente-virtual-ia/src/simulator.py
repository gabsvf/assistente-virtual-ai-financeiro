def calculate_compound_interest(initial, monthly, monthly_rate_percent, months):
    rate = monthly_rate_percent / 100
    balance = float(initial)
    principal = float(initial)
    for _ in range(int(months)):
        balance *= (1 + rate)
        balance += float(monthly)
        principal += float(monthly)
    return {
        "final_value": balance,
        "principal": principal,
        "interest": balance - principal,
    }

def calculate_loan(amount, monthly_rate_percent, months):
    amount = float(amount)
    rate = monthly_rate_percent / 100
    months = int(months)
    if rate == 0:
        installment = amount / months
    else:
        installment = amount * (rate * (1 + rate) ** months) / ((1 + rate) ** months - 1)
    return {"installment": installment, "total": installment * months}
