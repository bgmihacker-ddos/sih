from sqlalchemy.orm import Session
from app.models.coc import ChainOfCustodyEvent
import uuid

class CoCService:
    @staticmethod
    def log_event(db: Session, evidence_id: str, user_id: str, action: str, details: dict = None):
        event = ChainOfCustodyEvent(
            id=str(uuid.uuid4()),
            evidence_id=evidence_id,
            user_id=user_id,
            action=action,
            details=details
        )
        db.add(event)
        db.commit()
