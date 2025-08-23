import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core.config import settings
from .routers import predict as predict_router
from .routers import health as health_router
from .model_loader import load_model

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_title, version=settings.app_version)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router.router)
    app.include_router(predict_router.router)

    @app.on_event("startup")
    def on_startup():
        # start loading model in background so server binds quickly
        thread = threading.Thread(target=load_model, kwargs={}, daemon=True)
        thread.start()

    return app

app = create_app()
