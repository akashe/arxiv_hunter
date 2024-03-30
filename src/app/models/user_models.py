from datetime import datetime
from typing import Optional, Any

from pydantic import validator
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str = Field(max_length=256, min_length=6)
    email: str
    created_at: datetime = datetime.now()
    preferences: str = Field(default="")  # Added preferences field with default value as empty string

class UserInput(SQLModel):
    username: str
    password: str = Field(max_length=256, min_length=6)
    password2: str  # for confirmation
    email: str
    preferences: str = ""  # Added preferences field with default value as empty string

    @validator('password2')
    def password_match(cls, v, values, **kwargs) -> Any:
        if 'password' in values and v != values['password']:
            raise ValueError('passwords don\'t match')
        return v

class UserLogin(SQLModel):
    username: str
    password: str

class UserPreferences(SQLModel):
    preferences: str
