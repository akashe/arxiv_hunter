"""Entry Point for the FastAPI App"""
import os
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi import responses, status
from fastapi.templating import Jinja2Templates
import pandas as pd
from fastapi.staticfiles import StaticFiles

from src.logics.arxiv_recommender import LearnTransformVocabulary, Recommender
from src.logics import arxiv_search
from src.app import schemas
from src.logics.arxiv_recommender import LearnTransformVocabulary
# import sys
# sys.modules["__main__"].LearnTransformVocabulary = LearnTransformVocabulary


recommender = Recommender(vocabulary_path="data/transformed_data.pkl", vectorizer_path="data/vectorizer.pkl")
search = arxiv_search.ArxivSearcher()

BASE_PATH = Path(__file__).resolve().parent
print(f"BASE_PATH: {BASE_PATH}")

app = FastAPI()

TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))
app.mount("/static", StaticFiles(directory="src/static"), name="static")
@app.get(path="/")
def homepage(request: Request):
    return TEMPLATES.TemplateResponse(
        "home.html", {"request": request, "name": "Subrata Mondal"}
    )


# Define a route for searching documents
@app.get("/search", response_model=List[schemas.SearchResult])
def search_arxiv_papers(query: str = Query(default="LLM", min_length=3, max_length=64)):
    """Search through the Arxiv API"""
    # Validate the input and perform the search
    try:
        # perform search
        results = search.search(query=query, days=60, max_results=10)
    except Exception as e:
        # Return an error if something goes wrong
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
    # Return the results or an empty list if none are found
    if results:
        return responses.JSONResponse(content=results, status_code=status.HTTP_200_OK)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="No results found"
    )


# Define a route for getting recommendations
@app.get("/recommend", response_model=List[schemas.Recommendation])
def get_recommendations(query: str):
    """Arxiv Research Paper Recommendation"""
    vocabulary = LearnTransformVocabulary(
        json_data = "../../data/master_data.json"
    )
    # Validate the input and generate recommendations
    try:
        # Perform recommendation
        recommendations = recommender.recommend(query=query)
        # df = pd.read_json("data/master_data.json")
        # indexes = [index for index, _ in recommendations]
        # result = df.loc[indexes].values
    except Exception as e:
        # Return an error if something goes wrong
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
    # Return the recommendations
    return responses.JSONResponse(
        content=recommendations, status_code=status.HTTP_200_OK
    )


if __name__=="__main__":
    pass
