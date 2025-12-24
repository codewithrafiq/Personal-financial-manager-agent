from langchain.agents import create_agent
from langchain.messages import SystemMessage

from app.llm import get_llm
from app.tools import (
    add_transaction,
    analyze_expenses,
    handle_tool_errors,
    monthly_summary,
    our_services,
)


def get_agent():
    llm = get_llm()

    tools = [
        our_services,
        analyze_expenses,
        add_transaction,
        monthly_summary,
    ]

    tools_description = "\n".join(
        f"- {tool.name}: {tool.description}" for tool in tools
    )

    system_prompt = SystemMessage(
        content=(
            "You are a personal financial manager.\n"
            "Decide whether to call a tool or respond normally.\n"
            "Use tools when appropriate.\n\n"
            "Available tools:\n"
            f"{tools_description}"
        )
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        middleware=[handle_tool_errors],
        system_prompt=system_prompt,
    )
    if not agent:
        raise ValueError("Agent creation failed.")

    return agent
