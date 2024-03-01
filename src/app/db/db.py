from sqlmodel import create_engine, SQLModel


ENGINE = create_engine(
    url="sqlite:///database.db",
    echo=True # displays info in terminal related to changes in the database
)

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=ENGINE)