from fastapi import APIRouter, HTTPException, status

# from ..models.users import User
# rom ..schemas.users import UserCreate, UserLogin
from src.app.models.users import User
from src.app.schemas.users import UserCreate, UserLogin

users = APIRouter()

# mock database
db = {}


@users.post("/register", response_model=User)
def register_user(user: UserCreate):
    if user.username in db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
        )
    db[user.username] = user.password
    return User(username=user.username, password=user.password)


@users.post("/login", response_model=User)
def login_user(user: UserLogin):
    if user.username not in db or user.password != db[user.username]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return User(username=user.username, password=user.password)
