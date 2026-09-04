from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.models.case import Case, Evidence
from app.services.evidence_service import EvidenceService
from app.services.coc_service import CoCService
from app.security.auth import get_current_user
from app.security.rbac import RoleChecker
from app.models.user import Role
import uuid

router = APIRouter()
admin_or_analyst = RoleChecker(allowed_roles=[Role.ADMIN, Role.ANALYST])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", dependencies=[Depends(admin_or_analyst)])
def create_case(name: str, db: Session = Depends(get_db)):
    case = Case(id=str(uuid.uuid4()), name=name)
    db.add(case)
    db.commit()
    return case

@router.get("", dependencies=[Depends(get_current_user)])
def list_cases(db: Session = Depends(get_db)):
    return db.query(Case).all()

@router.post("/{case_id}/evidence", dependencies=[Depends(admin_or_analyst)])
async def upload(case_id: str, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if not db.query(Case).filter(Case.id == case_id).first():
        raise HTTPException(status_code=404, detail="Case not found")
    metadata = EvidenceService.save_evidence(file.file, file.filename)
    evidence = Evidence(
        id=metadata["evidence_id"],
        case_id=case_id,
        sha256=metadata["sha256"],
        original_filename=metadata["original_filename"],
        storage_path=metadata["storage_path"],
        file_size=metadata["size"],
        uploader_id=current_user["username"]
    )
    db.add(evidence)
    db.commit()
    CoCService.log_event(db, evidence.id, current_user["username"], "UPLOADED", {"filename": metadata["original_filename"]})
    return metadata

@router.post("/{case_id}/analyze", dependencies=[Depends(admin_or_analyst)])
async def analyze_case(case_id: str, db: Session = Depends(get_db)):
    # ... placeholder remaining same ...
    return {"status": "analyzed"}
