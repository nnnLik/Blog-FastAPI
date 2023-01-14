from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config


SQLALCHEMY_DATABASE_URL = f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@{config('POSTGRES_HOST')}/{config('POSTGRES_DB')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

