# lightweight, thread-safe loader + readiness check
from joblib import load
from threading import Lock
from pathlib import Path
from ..core.config import settings

_model = None
_model_lock = Lock()

def load_model(mmap_mode: str | None = None):
    """Load the model (idempotent). Optionally use mmap_mode='r' for large arrays."""
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                p: Path = settings.model_path
                if not p.exists():
                    raise FileNotFoundError(f"Model file not found: {p}")
                # For large arrays consider: load(p, mmap_mode='r')
                _model = load(p) if mmap_mode is None else load(p, mmap_mode=mmap_mode)
    return _model

def is_model_loaded() -> bool:
    return _model is not None

def get_model():
    """FastAPI dependency that will load the model if not loaded yet.
       (predict route uses Depends(get_model))"""
    return load_model()
