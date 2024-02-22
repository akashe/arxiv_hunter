"""Database Models: Represent SQL tables and relationships."""
import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database

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
    is_active = _sql.Column(_sql.Boolean, default=True)

    # relationship with 'Post' model
    posts = _orm.relationship("Post", back_populates="owner")

class Post(_database.BASE):
    """Represents a post created by a user.

    Maps to the "posts" table with columns for:
        - id: Unique identifier (primary key)
        - title: Title of the post
        - content: Content of the post
        - owner_id: Foreign key referencing the user who created the post
        - date_created: Date and time the post was created
        - date_last_updated: Date and time the post was last updated

    Belongs to the User model, meaning a post is created by a specific user.
    """
    __tablename__ = "posts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    content = _sql.Column(_sql.String, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    # relationship with User model
    owner = _orm.relationship("User", back_populates="posts")