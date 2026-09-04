from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class ChainOfCustodyEvent(Base):
    __tablename__ = "coc_events"

    id = Column(String, primary_key=True, index=True)
    evidence_id = Column(String, ForeignKey("evidence.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    timestamp = Column(DateTime, default=func.now())
    action = Column(String, nullable=False)
    details = Column(JSON, nullable=True)

    evidence = relationship("Evidence", back_populates="coc_events")
