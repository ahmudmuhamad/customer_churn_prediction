from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/ready")
def ready():
    # simple readiness; in production you might check model loaded / db connectivity
    return {"ready": True}