"""Entry Point for the FastAPI App"""

from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi import responses, status
from fastapi.templating import Jinja2Templates
from ..app import schemas

BASE_PATH = Path(__file__).resolve().parent
print(f"BASE_PATH: {BASE_PATH}")
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))

app = FastAPI()


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
        results = query
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
def get_recommendations(keywords: Optional[List[str]] = Query(max_length=16)):
    """Arxiv Research Paper Recommendation"""
    # Validate the input and generate recommendations
    try:
        # Perform recommendation
        recommendations = keywords
    except Exception as e:
        # Return an error if something goes wrong
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
    # Return the recommendations
    return responses.JSONResponse(
        content=recommendations, status_code=status.HTTP_200_OK
    )


# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run(app, port=8080, host="0.0.0.0")
