from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

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
    timestamp = Column(DateTime)
    filter_type = Column(String)
