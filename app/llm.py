from langchain_ollama import ChatOllama

from app.config import MODEL_NAME, OLLAMA_BASE_URL


def get_llm():
    return ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL_NAME, temperature=0.2)
