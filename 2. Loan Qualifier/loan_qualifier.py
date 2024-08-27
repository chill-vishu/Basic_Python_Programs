def loan_qualifier(income, credit_score, debt, loan_amount):
    if income > 50000 and credit_score > 700 and debt < loan_amount * 0.4:
        return "You qualify for the loan."
    else:
        return "You do not qualify for the loan."

# Example usage
print(loan_qualifier(60000, 720, 10000, 200000))