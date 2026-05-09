from langchain_core.tools import tool


@tool
def save_expense_advice(advice: str) -> str:
    """
    Save the advice on expenses to the database.
    """
    print("+-+-" * 20)
    print("Using tool: save_expense_advice")
    print("+-+-" * 20)
    return f"Expense advice saved: {advice}"
