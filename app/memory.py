from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage


def get_clean_history(session_id: str):
    history = SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///chat_memory.db",
    )

    # 🔑 Only keep valid chat messages
    return [
        m for m in history.messages if isinstance(m, (HumanMessage, AIMessage))
    ], history
