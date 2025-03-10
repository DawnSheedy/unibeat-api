from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.getenv(
    "POSTGRES_CONNECTION_STRING", "sqlite:///./sql_app.db"
)

engine = (
    create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite")
    else create_engine(SQLALCHEMY_DATABASE_URL)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
