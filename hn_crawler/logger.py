import json
import logging
from datetime import datetime
from hn_crawler.db import get_session
from hn_crawler.models import UsageLog

logger = logging.getLogger(__name__)


class UsageLogHandler:
    @staticmethod
    def log(filter_type: str, request_url: str, response_status_code: int, entries_scraped: int,
            error_message: str | None, filter_result_count: int, results: list[dict], session=None):
        close_session = False
        if session is None:
            session = get_session()
            close_session = True

        try:
            usage = UsageLog(timestamp=datetime.utcnow(),
                             filter_type=filter_type,
                             request_url=request_url,
                             response_status_code=response_status_code,
                             entries_scraped=entries_scraped,
                             error_message=error_message,
                             filter_result_count=filter_result_count,
                             results=json.dumps(results)
                             )
            session.add(usage)
            session.commit()
        except Exception as e:
            logger.error(f"Failed to log usage data: {e}", exc_info=True)
        finally:
            if close_session:
                session.close()

    @staticmethod
    def fetch_logs():
        session = get_session()
        try:
            logs = session.query(UsageLog).all()
            results = []
            for log in logs:
                results.append({
                    "id": log.id,
                    "timestamp": log.timestamp.isoformat(),
                    "filter_type": log.filter_type,
                    "request_url": log.request_url,
                    "response_status_code": log.response_status_code,
                    "entries_scraped": log.entries_scraped,
                    "error_message": log.error_message,
                    "filter_result_count": log.filter_result_count,
                    "results": json.loads(log.results),  # Convert JSON string back to object
                })
            return results
        finally:
            session.close()

    @staticmethod
    def fetch_last_log():
        session = get_session()
        try:
            log = session.query(UsageLog).order_by(UsageLog.timestamp.desc()).first()
            if log:
                return {
                    "id": log.id,
                    "timestamp": log.timestamp.isoformat(),
                    "filter_type": log.filter_type,
                    "request_url": log.request_url,
                    "response_status_code": log.response_status_code,
                    "entries_scraped": log.entries_scraped,
                    "error_message": log.error_message,
                    "filter_result_count": log.filter_result_count,
                    "results": json.loads(log.results),
                }
            return None
        finally:
            session.close()
