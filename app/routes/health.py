from fastapi import APIRouter

from app.core.config import settings


router = APIRouter(
    tags=["Health"]
)


@router.get("/health")
def health():

    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.VERSION
    }