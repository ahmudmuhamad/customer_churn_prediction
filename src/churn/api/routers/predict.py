from fastapi import APIRouter, Depends, HTTPException
from typing import List
import pandas as pd
import logging

from ..schemas import PredictRequest, PredictResponse
from ..model_loader import get_model
from ...core.config import settings

router = APIRouter(prefix="/predict", tags=["predict"])

logger = logging.getLogger(__name__)

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
        logger.exception("Bad input shape")
        raise HTTPException(status_code=400, detail=f"Bad input shape: {type(e).__name__}: {e}")

    try:
        proba = model.predict_proba(X)[:, 1].tolist()
    except Exception as e:
        logger.exception("Model prediction error")
        raise HTTPException(status_code=500, detail=f"Model prediction error: {type(e).__name__}: {e}")

    threshold = req.threshold if req.threshold is not None else settings.default_threshold
    predictions = [1 if p >= threshold else 0 for p in proba]

    return PredictResponse(predictions=predictions, probabilities=proba)