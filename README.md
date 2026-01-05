# Personal-financial-manager-agent



# RUN LLM LOCALLY
```
docker compose -f docker/docker-compose.yml up --build -d
docker exec -it ollama bash
ollama pull llama3.1:8b
```

# RUN THE APPLICATION
```
uvicorn app.main:app --port 8000 --reload
```