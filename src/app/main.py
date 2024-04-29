"""Entry Point for the FastAPI App"""

from pathlib import Path
from typing import List
from fastapi import FastAPI, HTTPException, Query, Request, Depends
from fastapi import responses, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

import fastapi as _fastapi
from . import services as _services
from . import schemas as _schemas
import sqlalchemy.orm as _orm
from .auth import auth
from .endpoints.user_endpoints import user_router
from .models.user_models import *

from .db.db import create_db_and_tables

from src.logics.arxiv_recommender import LearnTransformVocabulary, Recommender
from src.logics import arxiv_search
from src.app import schemas
from src.logics.arxiv_recommender import LearnTransformVocabulary

import sys
sys.modules["__main__"].LearnTransformVocabulary = LearnTransformVocabulary


recommender = Recommender(
        vectorizer_path="data/vectorizer.pkl",
        vocabulary_path="data/transformed_data.pkl",
    )

df = pd.read_pickle("data/master_data.pkl")

search = arxiv_search.ArxivSearcher()

BASE_PATH = Path(__file__).resolve().parent
print(f"BASE_PATH: {BASE_PATH}")

app = _fastapi.FastAPI()

app.include_router(user_router)
auth_handler = auth.AuthHandler()
create_db_and_tables()

origins = [
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))
TEMPLATES = Jinja2Templates(directory=BASE_PATH / "../templates")
app.mount("/static", StaticFiles(directory=BASE_PATH / "../static"), name="static")


@app.get(path="/")
def homepage(request: Request, user=Depends(auth_handler.auth_wrapper)):
    return TEMPLATES.TemplateResponse(
        name="index.html", context={"request": request, "name": "Subrata Mondal"}
    )

@app.get(path="/recommend", response_model=List[schemas.RecommendedPaper])
def get_recommendations(query: str = Query(default="LLM, Attention, GPT"), user=Depends(auth_handler.auth_wrapper)):
    """Arxiv Research Paper Recommendation"""
    try:
        # Perform validation and recommendation steps (refer to previous responses for details)
        recommendations = recommender.recommend(query=query)
        recommended_papers = []

        # Create RecommendedPaper instances for each recommendation
        for index in recommendations:
            paper_data = df.iloc[index].to_dict()
            recommended_papers.append(schemas.RecommendedPaper(**paper_data))

        return recommended_papers

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e

app.include_router(router=user_router)