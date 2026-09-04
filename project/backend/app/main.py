from fastapi import FastAPI
from app.api import auth, cases, graph

app = FastAPI(title="FORENSIGHT SIH V2")
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(cases.router, prefix="/api/cases", tags=["cases"])
app.include_router(graph.router, prefix="/api/graph", tags=["graph"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
