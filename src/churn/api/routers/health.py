from fastapi import APIRouter
# import only the readiness checker (avoid importing heavy libs here)
from ..model_loader import is_model_loaded

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/ready")
def ready():
    # returns True only after model loaded by background thread
    return {"ready": is_model_loaded()}
