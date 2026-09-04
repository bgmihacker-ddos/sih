from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EvidenceBase(BaseModel):
    case_id: str
    original_filename: str

class EvidenceCreate(EvidenceBase):
    pass

class EvidenceMetadata(BaseModel):
    evidence_id: str
    sha256: str
    md5: str
    size: int
    created_at: datetime
