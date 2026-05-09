from typing import Annotated

from langchain_core.tools import tool


@tool
def add_transaction(
    amount: Annotated[float, "The transaction amount"],
    category: Annotated[str, "The expense or income category"],
    note: Annotated[str, "Optional note or description"] = "",
) -> str:
    """Add a financial transaction."""
    print("+-+-" * 20)
    print("Using tool: add_transaction")
    print("+-+-" * 20)
    return f"Added transaction: {amount} in {category}. Note: {note}"
