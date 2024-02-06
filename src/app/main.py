"""Entry Point for the FastAPI App"""

from typing import List, Optional
from fastapi import FastAPI, HTTPException, responses, status, Query
from src.app import schemas

app = FastAPI()


@app.get(path="/", response_class=responses.HTMLResponse)
def homepage():
    body = """
        <html>
            <head>
                <style>
                    h1 {
                        text-align: center;
                    }
                    form {
                        display: block;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to Arxiv Hunter</h1>
                <!-- Use a form tag with the action and method attributes -->
                <form action="http://127.0.0.1:8000/search" method="GET">
                    <!-- Use an input tag with the type, name, and placeholder attributes -->
                    <input type="text" name="query" placeholder="Attention is all you need.">
                    <!-- Use an input tag with the type and value attributes -->
                    <input type="submit" value="Search">
                </form>
                <!-- Use another form tag with the action and method attributes -->
                <form action="http://127.0.0.1:8000/recommend" method="GET">
                    <!-- Use another input tag with the type, name, and placeholder attributes -->
                    <input type="text" name="keywords" placeholder="LLM, Attention, GPT">
                    <!-- Use another input tag with the type and value attributes -->
                    <input type="submit" value="Recommend">
                </form>
            </body>
        </html>
    """
    return responses.HTMLResponse(content=body)


# Define a route for searching documents
@app.get("/search", response_model=List[schemas.SearchResult])
def search_arxiv_papers(query:str = Query(default="LLM", min_length=3, max_length=64)):
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
def get_recommendations(keywords:Optional[List[str]] = Query(max_length=16)):
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
