"""Schemas: Define data representations for API requests/responses.
This separation improves data validation and control over what data 
is exposed through the API.
"""

import datetime as _dt
import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    """Base schema for User data, including email."""
    email: str


class UserCreate(_UserBase):
    """Schema for creating a new User.
    Requires email and password, used for data validation and creation.
    """
    password: str


class User(_UserBase):
    """Schema for representing a User including additional details and posts.
    Inherits from _UserBase and adds fields like ID, active status, and a list of posts.
    """
    preferences:str

    id: int
    is_active: bool

    class Config:
        from_attributes = True


class RecommendedPaper(_pydantic.BaseModel):
    """Base schema for RecommendedPaper data, including basic paper details."""
    id: str
    title: str
    published_date: _dt.datetime
    pdf_link: _pydantic.HttpUrl
    summary: str
    pdf_text: str
