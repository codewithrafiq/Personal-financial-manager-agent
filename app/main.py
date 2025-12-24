from fastapi import FastAPI
from langchain.messages import HumanMessage

from app.agent import get_agent
from app.schemas import QueryRequest
from app.tools import get_final_text

app = FastAPI(title="Personal Financial Manager API", version="0.1.0")

agent = get_agent()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Financial Manager API!"}


@app.post("/query")
def process_query(request: QueryRequest):
    query = request.query
    print("Received query:", query)
    response = agent.invoke({"messages": [HumanMessage(query)]})
    return get_final_text(response.get("messages", []))
