from typing import Annotated

from langchain_core.tools import tool


@tool
def analyze_expenses(
    expenses: Annotated[str, "A natural language description of expenses to analyze"],
) -> str:
    """Analyze a list of expenses and give insights."""
    print("+-+-" * 20)
    print("Using tool: analyze_expenses")
    print("+-+-" * 20)
    return f"Expense analysis completed for: {expenses}"
