import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

# llama-server OpenAI-compatible endpoint
# In Docker: set via LLAMA_SERVER_URL env var in docker-compose.yml
# Locally:   run llama-server manually then set LLAMA_SERVER_URL=http://localhost:8080/v1
LLAMA_SERVER_URL = os.getenv("LLAMA_SERVER_URL", "http://llama-cpp:8080/v1")
