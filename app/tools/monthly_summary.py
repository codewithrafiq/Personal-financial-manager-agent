from typing import Annotated

from langchain_core.tools import tool


@tool
def monthly_summary(
    month: Annotated[str, "The month to summarize (e.g., January, February)"],
) -> str:
    """Summarize spending for a given month."""
    print("+-+-" * 20)
    print("Using tool: monthly_summary")
    print("+-+-" * 20)
    return f"Summary generated for {month}"
