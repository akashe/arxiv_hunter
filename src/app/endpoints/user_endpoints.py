from typing import Any

from fastapi import APIRouter, HTTPException, status, responses
from sqlmodel import Session

from ..auth import auth
from ..models.user_models import UserInput, User, UserLogin
from ..repos.user_repos import select_all_users, find_user
from ..db.db import ENGINE

user_router = APIRouter()
auth_handler = auth.AuthHandler()
session = Session(bind=ENGINE)

@user_router.post(
        path="/register", 
        status_code=status.HTTP_201_CREATED, 
        tags=["users"],
        description="Register new user"
    )
def register(user:UserInput):
    all_users: Any = select_all_users(engine=ENGINE)
    if all_users:
        if any(x.username == user.username for x in all_users):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
    # encrypt password
    hash_password:str = auth_handler.get_password_hash(password=user.password)
    # create user
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password
    )
    session.add(instance=new_user)
    session.commit()
    return responses.JSONResponse(status_code=status.HTTP_201_CREATED, content="Successful user creation")

@user_router.post(
        path="/login", 
        status_code=status.HTTP_201_CREATED, 
        tags=["users"],
        description="Login user"
    )
def login(user:UserLogin):
    user_found = find_user(engine=ENGINE, name=user.username)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    verified = auth_handler.verify_password(password=user.password, hashed_password=user_found.password)
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    # if everything is fine till here, create token
    token = auth_handler.encode_token(user_id=user.username)
    return {"token":token}