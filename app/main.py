from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import HumanMessage

from app.agent import get_agent
from app.schemas import QueryRequest
from app.tools.utils import get_final_text

app = FastAPI(title="Personal Financial Manager API", version="0.1.0")

agent = get_agent()

# Serve static files
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/")
def read_root():
    """Serve the chat interface."""
    static_file = Path(__file__).parent / "static" / "index.html"
    if static_file.exists():
        return FileResponse(static_file)
    return {"message": "Welcome to the Personal Financial Manager API!"}


@app.post("/query")
def process_query(request: QueryRequest):
    query = request.query
    print("Received query:", query)
    response = agent.invoke({"messages": [HumanMessage(query)]})
    result = get_final_text(response.get("messages", []))
    # Convert response key to output for frontend compatibility
    return {"output": result.get("response", "No response generated.")}
