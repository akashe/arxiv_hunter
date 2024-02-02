from fastapi import APIRouter, Depends
from ..models.papers import Paper
from ..schemas.papers import PaperSearch, PaperRecommend

papers = APIRouter()

@papers.post("/search", response_model=list[Paper])
def search_papers(paper: PaperSearch = Depends()):
    # call the search_paper function from app/logic/paper.py
    return {
        "paper": paper
    }

@papers.get("/recommend/{paper_id}", response_model=list[Paper])
def recommend_papers(paper_id: str):
    # call the recommend_paper function from app/logic/paper.py
    return paper_id
