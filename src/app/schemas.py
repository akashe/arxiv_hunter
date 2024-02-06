"""Schemas using Pydantic for Request and Response Model"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, HttpUrl




# Define a response model for the search results
class SearchResult(BaseModel):
    """Response Model for the Search Result"""

    title: str
    pdf_link: HttpUrl


# Define a response model for the recommendations
class Recommendation(BaseModel):
    """Response Model for the Recommendation"""

    items: List[Dict[str, Any]]
