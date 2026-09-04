from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    evidence = relationship("Evidence", back_populates="case")

class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), nullable=False)
    sha256 = Column(String, nullable=False)
    md5 = Column(String, nullable=True) # Legacy identifier
    original_filename = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    mime_type = Column(String, nullable=True)
    file_size = Column(BigInteger, nullable=False)
    uploader_id = Column(String, ForeignKey("users.id"), nullable=False)
    upload_timestamp = Column(DateTime, default=func.now())

    case = relationship("Case", back_populates="evidence")
    coc_events = relationship("ChainOfCustodyEvent", back_populates="evidence")
