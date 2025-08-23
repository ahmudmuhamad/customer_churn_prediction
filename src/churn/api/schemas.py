from typing import List, Dict, Union
from pydantic import BaseModel, Field


class FeatureSet(BaseModel):
    # Regular model for feature validation
    features: Dict[str, float]


class PredictRequest(BaseModel):
    # Accept either a single record or a list (batch)
    data: Union[FeatureSet, List[FeatureSet]] = Field(..., description="Single feature set or list of feature sets")
    threshold: float = Field(0.5, ge=0.0, le=1.0, description="Classification threshold")


class PredictResponse(BaseModel):
    predictions: List[int] = Field(..., description="Binary predictions (0 or 1)")
    probabilities: List[float] = Field(..., description="Prediction probabilities between 0 and 1")