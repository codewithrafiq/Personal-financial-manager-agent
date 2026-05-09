from langchain_core.tools import tool


@tool
def advice_on_expenses() -> str:
    """
    Provide advice on expenses. Before giving advice, ask the user:
    - What kind of expenses they want advice on
    - What is their current spending pattern
    - What is their financial goal
    - What is their current budget for expenses

    Once the user provides this information, give advice and call
    save_expense_advice to save it.
    """
    print("+-+-" * 20)
    print("Using tool: advice_on_expenses")
    print("+-+-" * 20)
    return "To provide advice on expenses, please share details about your spending patterns, financial goals, and budget."
