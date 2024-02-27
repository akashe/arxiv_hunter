"""Database Models: Represent SQL tables and relationships."""

import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from . import database as _database


class User(_database.BASE):
    """Represents a user in the database.

    Maps to the "users" table with columns for:
        - id: Unique identifier (primary key)
        - email: User's email address (unique)
        - hashed_password: Hashed password for security
        - is_active: Boolean flag indicating if the user is active

    Has a one-to-many relationship with the Post model, meaning a user can create many posts.
    """

    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    preferences = _sql.Column(_sql.String, default="")
    is_active = _sql.Column(_sql.Boolean, default=True)