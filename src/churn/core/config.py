from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path


class Settings(BaseSettings):
    model_path: Path = Field(default=Path(r"E:\customer_churn_prediction\models\final_xgb.joblib"))
    default_threshold: float = Field(default=0.5)
    app_title: str = Field(default="Churn prediction API")
    app_version: str = Field(default="0.1.0")
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


# Create settings instance
settings = Settings()