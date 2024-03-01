"""repo to get users data from db"""

from sqlmodel import Session, select

from ..db.db import ENGINE
from ..models.user_models import User

def select_all_users(engine):
    with Session(bind=engine) as session:
        statement = select(User)
        result = session.exec(statement=statement).all()

def find_user(engine, name):
    with Session(bind=engine) as session:
        statement = select(User).where(User.username==name)
        return session.exec(statement=statement).first()