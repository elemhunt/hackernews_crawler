from datetime import datetime
from hn_crawler.db import get_session
from hn_crawler.models import UsageLog


class UsageLogHandler:
    @staticmethod
    def log(filter_type: str):
        session = get_session()
        log = UsageLog(timestamp=datetime.utcnow(), filter_type=filter_type)
        session.add(log)
        session.commit()
        session.close()
