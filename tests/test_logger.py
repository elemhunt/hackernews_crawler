import pytest
import json
from hn_crawler.logger import UsageLogHandler
from hn_crawler.models import UsageLog

@pytest.fixture
def patch_get_session(monkeypatch, test_db):
    monkeypatch.setattr("hn_crawler.logger.get_session", test_db.get_session)
    yield

def test_log_and_fetch(test_db, patch_get_session):
    UsageLogHandler.log(
        filter_type="test_filter",
        request_url="https://example.com",
        response_status_code=200,
        entries_scraped=5,
        error_message=None,
        filter_result_count=3,
        results=[{"sample": "data"}]
    )
    session = test_db.get_session()
    log = session.query(UsageLog).order_by(UsageLog.id.desc()).first()
    assert log is not None
    assert log.filter_type == "test_filter"
    assert json.loads(log.results) == [{"sample": "data"}]
    session.close()

def test_fetch_logs(test_db, patch_get_session):
    logs = UsageLogHandler.fetch_logs()
    assert isinstance(logs, list)
    assert len(logs) >= 1
    log = logs[-1]
    assert "timestamp" in log
    assert "filter_type" in log
    assert "results" in log
