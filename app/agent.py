from langgraph.prebuilt import create_react_agent

from app.llm import get_llm


def get_agent():
    llm = get_llm()

    # TODO: Re-enable tools once llama.cpp API properly supports tool schemas
    tools = []

    system_prompt = (
        "You are a helpful personal financial manager assistant. "
        "Answer questions about personal finance, budgeting, and money management."
    )

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,
    )

    return agent
