from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:development_password@db:5432/foresight")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import all models here so Alembic detects them
from app.models.user import User
from app.models.case import Case, Evidence
from app.models.coc import ChainOfCustodyEvent
