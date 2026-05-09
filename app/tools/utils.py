from langchain_core.messages import AIMessage, ToolMessage


def get_final_text(messages: list) -> dict:
    """Extract the last AI text response from the message list."""
    for msg in reversed(messages):
        if (
            isinstance(msg, AIMessage)
            and isinstance(msg.content, str)
            and msg.content.strip()
        ):
            return {"response": msg.content}
    return {"response": "No response generated."}


def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return handler(request)
    except Exception as e:
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"],
        )
