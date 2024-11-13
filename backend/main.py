# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.search_agent import search_papers
from agents.database_agent import store_paper_in_db, query_papers_by_year
from agents.qa_agent import answer_question
from agents.future_works_agent import generate_future_works

app = FastAPI()

# Data model for storing paper data
class Paper(BaseModel):
    title: str
    abstract: str
    year: int

# Data model for question request
class QuestionRequest(BaseModel):
    question: str
    context: str

# Endpoint to search and store papers
@app.get("/search_papers")
async def search_papers_endpoint(query: str):
    papers = search_papers(query)
    for paper in papers:
        store_paper_in_db(paper)  # Store each paper in the database
    return {"papers": papers}

# Endpoint to store a single paper manually
@app.post("/store_paper")
async def store_paper_endpoint(paper: Paper):
    store_paper_in_db(paper.dict())
    return {"message": "Paper stored successfully"}

# Endpoint to query papers by year
@app.get("/query_papers/{year}")
async def query_papers_endpoint(year: int):
    papers = query_papers_by_year(year)
    return {"papers": papers}

# Q&A endpoint to answer questions based on context
@app.post("/answer_question")
async def answer_question_endpoint(request: QuestionRequest):
    try:
        answer = answer_question(request.context, request.question)
        return {"answer": answer.get("answer", "No answer found")}
    except Exception as e:
        return {"error": str(e)}

# Endpoint to generate future research ideas based on context
@app.post("/generate_future_works")
async def generate_future_works_endpoint(context: str):
    future_works = generate_future_works(context)
    return {"future_works": future_works}
