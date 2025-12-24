from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage
from langchain_core.tools import tool


@tool
def analyze_expenses(expenses: str) -> str:
    """
    Analyze a list of expenses and give insights.
    Input should be a natural language description of expenses.
    """
    return f"Expense analysis completed for: {expenses}"


@tool
def add_transaction(amount: float, category: str, note: str = "") -> str:
    """
    Add a financial transaction.
    """
    # Later: save to DB
    return f"Added transaction: {amount} in {category}. Note: {note}"


@tool
def monthly_summary(month: str) -> str:
    """
    Summarize spending for a given month.
    """
    return f"Summary generated for {month}"


@tool
def our_services() -> str:
    """
    List the financial services we offer.
    """
    services = [
        "Expense Analysis",
        "Budget Planning",
        "Savings Advice",
        "Transaction Tracking",
        "Financial Goal Setting",
        "Advice on Expenses",
        "Advice on Savings",
        "Advice on Budgets",
    ]
    return "Our services include: " + ", ".join(services)


@tool
def advice_on_expenses() -> str:
    """
    if user need advice on expenses service then we need to some query from the user
    - what kind of expenses they want advice on
    - what is their current spending pattern
    - what is her financial goal
    - what is her current budget for expenses


    and if user provide this information then we can give them advice on expenses then call save_expense_advice function to save the advice in the database
    """
    return "To provide advice on expenses, please share details about your spending patterns, financial goals, and budget."


@tool
def save_expense_advice(advice: str) -> str:
    """
    Save the advice on expenses to the database.
    """
    # Later: save to DB
    return f"Expense advice saved: {advice}"


@wrap_tool_call
def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return handler(request)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"],
        )


def get_final_text(messages):
    for msg in reversed(messages):
        if msg.type == "ai" and msg.content:
            return msg.content
    return ""
