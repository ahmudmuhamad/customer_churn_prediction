from fastapi import APIRouter, Depends, HTTPException
from typing import List
import pandas as pd

from ..schemas import PredictRequest, PredictResponse
from ..model_loader import get_model
from ...core.config import settings

router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/", response_model=PredictResponse)
def predict(req: PredictRequest, model=Depends(get_model)):
    # normalize to list of dicts
    if isinstance(req.features, dict):
        records = [req.features]
    else:
        records = req.features

    try:
        X = pd.DataFrame(records)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad input shape: {e}")

    try:
        # Typical scikit-learn / XGBoost interface
        proba = model.predict_proba(X)[:, 1].tolist()
    except AttributeError:
        # If your model only supports predict (no probabilities) fall back to that
        preds = model.predict(X).tolist()
        proba = [float(p) for p in preds]

    threshold = req.threshold if req.threshold is not None else settings.default_threshold
    predictions = [1 if p >= threshold else 0 for p in proba]

    return PredictResponse(predictions=predictions, probabilities=proba)