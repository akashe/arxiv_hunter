"""Database: Manages connection and sessions for SQLite database."""
import sqlalchemy as _sql

import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# database connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# engine for connecting to the database
ENGINE: _sql.Engine = _sql.create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# session maker for opening database sessions
SESSION_LOCAL = _orm.sessionmaker(
    bind=ENGINE, # bind the session maker to the engine
    autoflush=False, # disable automatic flushing for performance optimization
    autocommit=False # prevent automatic commits for better control
)

# base class for your database models
BASE = _declarative.declarative_base()