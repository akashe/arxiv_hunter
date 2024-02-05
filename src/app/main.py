from typing import List
from fastapi import FastAPI, Query, status
from src.app.schemas import SearchPaperResponseSchema, RecommendPaperResponseSchema
from src.logics.user import User, Recommender

app = FastAPI()


@app.get("/")
async def home():
    """Homepage"""
    return "Welcome to Arxiv Hunter: Feed"


user = User(preference={}, recommender=Recommender(data="../../data/master_data.pkl"))


@app.get(
    path="/search",
    status_code=status.HTTP_200_OK,
    response_model=List[SearchPaperResponseSchema],
)
async def search(
    query: str = Query(default="Attention, Mechanism, LLM"),
) -> List[SearchPaperResponseSchema]:
    """Search Research Papers"""
    print(user.search(query=query))
    return [{"id": "some_id", "title": "some_title"}]


@app.get(
    path="/recommend",
    status_code=status.HTTP_200_OK,
    response_model=List[RecommendPaperResponseSchema],
)
async def recommend(
    query: str = Query(default="Attention, Mechanism, LLM"),
) -> [RecommendPaperResponseSchema]:
    """Recommend Research Papers"""
    print(query)
    return [{"id": "some_id", "title": "some_title"}]
