# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database (file-based)
DATABASE_URL = "sqlite:///./weather.db"

# Engine create
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
