"""Entry Point for the FastAPI App"""

import json
from pathlib import Path
from typing import List
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi import responses, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import fastapi as _fastapi
import services as _services
import schemas as _schemas
import sqlalchemy.orm as _orm

from src.logics.arxiv_recommender import LearnTransformVocabulary, Recommender
from src.logics import arxiv_search
from src.app import schemas
from src.logics.arxiv_recommender import LearnTransformVocabulary

# import sys
# sys.modules["__main__"].LearnTransformVocabulary = LearnTransformVocabulary


recommender = Recommender(
    vocabulary_path="data/transformed_data.pkl", vectorizer_path="data/vectorizer.pkl"
)
search = arxiv_search.ArxivSearcher()

BASE_PATH = Path(__file__).resolve().parent
print(f"BASE_PATH: {BASE_PATH}")

app = _fastapi.FastAPI()
_services.create_database()

# TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))
TEMPLATES = Jinja2Templates(directory=BASE_PATH / "../templates")
app.mount("/static", StaticFiles(directory=BASE_PATH / "../static"), name="static")


@app.get(path="/")
def homepage(request: Request):
    return TEMPLATES.TemplateResponse(
        name="index.html", context={"request": request, "name": "Subrata Mondal"}
    )

@app.post(path="/users/", response_model=_schemas.User)
def create_user(user:_schemas.UserCreate, db:_orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=_fastapi.status.HTTP_400_BAD_REQUEST,
            detail="User already exists!!!"
        )
    return _services.create_user(db=db, user=user)

# Define a route for getting recommendations
@app.get("/recommend", response_model=List[schemas.RecommendedPaper])
def get_recommendations(
    request: Request, query: str = Query(default="LLM, Attention, GPT")
):
    """Arxiv Research Paper Recommendation"""
    vocabulary = LearnTransformVocabulary(json_data="../../data/master_data.json")
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


if __name__ == "__main__":
    pass
