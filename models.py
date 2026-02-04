from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ScamLog(Base):
    __tablename__ = "scam_logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    scam_type = Column(String)
    keywords = Column(String)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
