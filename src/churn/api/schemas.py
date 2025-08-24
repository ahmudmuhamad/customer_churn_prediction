from typing import List, Dict, Union
from pydantic import BaseModel, Field, model_validator


class FeatureSet(BaseModel):
    # Regular model for feature validation
    features: Dict[str, float]


class PredictRequest(BaseModel):
    features: Union[Dict[str, float], List[Dict[str, float]]] = Field(..., description="Feature dict or list of feature dicts")
    threshold: float = Field(0.5, ge=0.0, le=1.0)

    @model_validator(mode='before')
    @classmethod
    def accept_data_or_features(cls, values):
        # allow clients to send either "data" or "features"
        if "data" in values and "features" not in values:
            values["features"] = values.pop("data")
        return values


class PredictResponse(BaseModel):
    predictions: List[int] = Field(..., description="Binary predictions (0 or 1)")
    probabilities: List[float] = Field(..., description="Prediction probabilities between 0 and 1")