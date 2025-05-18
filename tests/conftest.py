import os
import pytest
from hn_crawler.db import Database

@pytest.fixture(scope="module")
def test_db():
    # Use a local test SQLite file path (not a URI)
    test_db_path = "test_usage.db"

    # Clean up before starting tests
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    # Instantiate the Database with the file path (not full URI)
    db = Database(test_db_path)

    yield db

    # Clean up after tests finish
    db.dispose()
    if os.path.exists(test_db_path):
        os.remove(test_db_path)
