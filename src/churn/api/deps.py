from fastapi import Depends
from .model_loader import get_model as _get_model


def get_model():
    return _get_model()