from langchain_core.tools import tool


@tool
def our_services() -> str:
    """List the financial services we offer."""
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
    print("+-+-" * 20)
    print("Using tool: our_services")
    print("+-+-" * 20)
    return "Our services include: " + ", ".join(services)
