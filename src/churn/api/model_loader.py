from joblib import load
from threading import Lock
from pathlib import Path
from ..core.config import settings


_model = None
_model_lock = Lock()

def load_model() -> object:
    """Load the model once (thread-safe). Returns the model object."""
    global _model
    if _model is None:
        with _model_lock:
         if _model is None:
            path: Path = settings.model_path
    if not path.exists():
        raise FileNotFoundError(f"Model file not found: {path}")
    _model = load(path)
    return _model


def get_model():
    """Dependency helper for FastAPI DI."""
    return load_model()