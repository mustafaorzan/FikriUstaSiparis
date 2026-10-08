from fastapi import FastAPI
from app.routes import siparis, takvim
from app.routes.musteri import router as musteri_router
from app.database import Base, engine
from app.models import Musteri, Siparis, Yikama, Ilaclama
from app.routes.dashboard import router as dashboard_router
from app.core.exception_handler import register_exception_handlers
from app.core.config import settings
from app.routes.health import router as health_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)

register_exception_handlers(app)
app.include_router(dashboard_router)
app.include_router(siparis.router)
app.include_router(takvim.router)
app.include_router(musteri_router)
app.include_router(health_router)

@app.get("/")
def home():
    return {
        "app": "Fikri Usta Sipariş Sistemine Hoşgeldiniz"
    }
