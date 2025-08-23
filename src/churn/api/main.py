from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core.config import settings
from .routers import predict as predict_router
from .routers import health as health_router
from .model_loader import load_model


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_title, version=settings.app_version)

    # CORS (adjust origins in production)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # include routers
    app.include_router(health_router.router)
    app.include_router(predict_router.router)

    @app.on_event("startup")
    def on_startup():
        # eagerly load model so readiness probes can verify it
        load_model()

    return app


app = create_app()