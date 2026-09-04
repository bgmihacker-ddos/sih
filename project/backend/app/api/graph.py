from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.models.case import Case, Evidence

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{case_id}/graph")
def get_graph(case_id: str, db: Session = Depends(get_db)):
    # Basic graph nodes: Case -> Evidence
    case = db.query(Case).filter(Case.id == case_id).first()
    nodes = [{"id": case.id, "label": case.name, "type": "case"}]
    edges = []

    for e in case.evidence:
        nodes.append({"id": e.id, "label": e.original_filename, "type": "evidence"})
        edges.append({"from": case.id, "to": e.id, "relationship": "contains"})

    return {"nodes": nodes, "edges": edges}
