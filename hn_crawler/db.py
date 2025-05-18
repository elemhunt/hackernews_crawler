import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hn_crawler.models import Base

DB_PATH = os.getenv("DB_PATH", "usage.db")
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()
