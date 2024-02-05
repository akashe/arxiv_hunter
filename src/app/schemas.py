"""Schemas - Pydantic Models for Request, Response Model"""

from pydantic import BaseModel


class SearchPaperResponseSchema(BaseModel):
    "Schema for the Research Paper"
    id: str
    title: str


class RecommendPaperResponseSchema(BaseModel):
    "Schema for the Research Paper"
    id: str
    title: str
