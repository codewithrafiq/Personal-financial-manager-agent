from langchain_openai import ChatOpenAI

from app.config import LLAMA_SERVER_URL


def get_llm():
    # Connect to llama-server's OpenAI-compatible endpoint.
    # Start the server first: see start.py or run.md
    return ChatOpenAI(
        model="local",
        base_url=LLAMA_SERVER_URL,
        api_key="not-needed",
        temperature=0.2,
    )
