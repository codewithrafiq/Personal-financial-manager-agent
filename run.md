# Run Guide

## Prerequisites

- Docker + Docker Compose installed on the Linux machine
- Ports `8000` and `8080` available
- Internet access on first run (model download ~660MB)

## Start

```bash
docker compose -f docker/docker-compose.yml up --build -d
```

On first run, the `model-downloader` service downloads the model into a persistent Docker volume. This only happens once.

## Watch logs

```bash
# All services
docker compose -f docker/docker-compose.yml logs -f

# API only
docker compose -f docker/docker-compose.yml logs -f api

# llama-cpp server only
docker compose -f docker/docker-compose.yml logs -f llama-cpp
```

## Check status

```bash
docker compose -f docker/docker-compose.yml ps
```

## Test

```bash
curl http://localhost:8000/

curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What services do you offer?"}'
```

## Stop

```bash
docker compose -f docker/docker-compose.yml down
```

## Change the model

Edit `docker/docker-compose.yml` under `model-downloader` → `command`, replace the URL with any GGUF model from HuggingFace. Then reset the volume and restart:

```bash
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up --build -d
```

## Development (auto-rebuild on file change)

Requires [nodemon](https://nodemon.io) installed on the host:

```bash
nodemon
```

Watches `app/` and `docker/` — rebuilds and restarts the API container on any `.py` or `dockerfile` change.
