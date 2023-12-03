from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

DATABASE_URL = "sqlite:///./assesment.db"
database = Database(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, unique=True),
    Column("age", String, unique=True)
)

engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)