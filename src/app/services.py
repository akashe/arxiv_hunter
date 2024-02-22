"""Database Services: Manage database creation and interaction.
This module provides a function for creating the database tables 
and acts as a middleman between your API and the database.
"""

import sqlalchemy.orm as _orm
from passlib.context import CryptContext

import database as _database
import models as _models
import schemas as _schemas


def create_database():
    """Creates all database tables based on defined models.

    Connects to the database using the `_database.ENGINE` object 
    and uses the metadata from `_database.BASE` to create all tables 
    defined in your models. This ensures the database structure exists 
    before your API starts using it.
    """
    return _database.BASE.metadata.create_all(bind=_database.ENGINE)

def get_db():
    """Opens a database session for secure database operations.
    Creates a database session using `_database.SESSION_LOCAL`, allowing 
    secure interaction with the database. The session is automatically closed 
    after use within a `with` block, ensuring proper resource management.
    """
    db = _database.SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db:_orm.Session, email:str):
    """Retrieves a user from the database by email."""
    return db.query(_models.User).filter(_models.User.email == email).first()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create_user(db:_orm.Session, user:_schemas.UserCreate):
    """Creates a new user in the database, securely hashing the password."""
    hashed_password = pwd_context.hash(user.password)
    db_user = _models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user