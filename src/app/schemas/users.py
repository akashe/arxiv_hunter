from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
