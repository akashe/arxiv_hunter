"""Schemas: Define data representations for API requests/responses.
This separation improves data validation and control over what data 
is exposed through the API.
"""

import datetime as _dt
import pydantic as _pydantic


class _PostBase(_pydantic.BaseModel):
    """Base schema for 'Post' data, including title and content."""

    title: str
    content: str


class CreatePost(_PostBase):
    """Schema for creating a new Post.
    Requires title and content, used for data validation and creation.
    """


class Post(_PostBase):
    """Schema for representing a Post including additional details.
    Inherits from '_PostBase' and adds fields like ID, owner ID,
    creation and update dates.
    """

    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True


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

    id: int
    is_active: bool
    posts: list[Post] = []

    class Config:
        orm_mode = True


class RecommendedPaper(_pydantic.BaseModel):
    """Base schema for RecommendedPaper data, including basic paper details."""

    id: str
    title: str
    published_date: _dt.datetime
    pdf_link: _pydantic.HttpUrl
    summary: str
    pdf_text: str
