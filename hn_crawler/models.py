from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

Base = declarative_base()


class Entry:
    def __init__(self, rank, title, points, comments):
        self.rank = rank
        self.title = title
        self.points = points
        self.comments = comments

    def __repr__(self):
        return f"<Entry(rank={self.rank}, title={self.title}, points={self.points}, comments={self.comments})>"


class UsageLog(Base):
    __tablename__ = "usage_logs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    filter_type = Column(String, nullable=False)

    request_url = Column(String, nullable=False)
    response_status_code = Column(Integer, nullable=False)
    entries_scraped = Column(Integer, nullable=False)
    error_message = Column(Text, nullable=True)
    filter_result_count = Column(Integer, nullable=False)

    results = Column(Text, nullable=False)  #   JSON stored as a string



