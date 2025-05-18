import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hn_crawler.models import Base


class Database:
    def __init__(self, db_path: str | None = None):
        if db_path is None:
            db_path =  os.getenv("DB_PATH") or os.getenv("TEST_DB_PATH") or "./usage.db"

        self._uri = self._make_sqlite_uri(db_path)
        self._engine = create_engine(self._uri, connect_args={"check_same_thread": False})
        self._SessionLocal = sessionmaker(bind=self._engine)

        # Ensure tables are created
        Base.metadata.create_all(bind=self._engine)

    @staticmethod
    def _make_sqlite_uri(path: str) -> str:
        p = Path(path).expanduser().resolve()
        p.parent.mkdir(parents=True, exist_ok=True)
        return "sqlite:///" + p.as_posix()  # Always use forward slashes for URI

    def get_session(self):
        return self._SessionLocal()


    def dispose(self):
        if self._engine:
            self._engine.dispose()

# Instantiate only once at import time for app use
db = Database()


def get_session():
    """Access shared DB session (for app usage)"""
    return db.get_session()
