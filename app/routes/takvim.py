from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.takvim import TakvimItemResponse
from app.services.takvim_service import TakvimService

router = APIRouter(
    prefix="/takvim",
    tags=["Takvim"]
)


@router.get(
    "/haftalik",
    response_model=list[TakvimItemResponse]
)
def haftalik_siparisler(
    baslangic: date | None = None,
    db: Session = Depends(get_db)
):

    return TakvimService.haftalik_getir(
        db,
        baslangic
    )

@router.get(
    "/gunluk",
    response_model=list[TakvimItemResponse]
)
def gunluk_takvim(
    tarih: date,
    db: Session = Depends(get_db)
):
    return TakvimService.gunluk_getir(
        db,
        tarih
    )

@router.get(
    "/bugun",
    response_model=list[TakvimItemResponse]
)
def bugunku_takvim(
    db: Session = Depends(get_db)
):
    return TakvimService.bugunku_getir(db)

@router.get(
    "/aralik",
    response_model=list[TakvimItemResponse]
)
def tarih_araligi(
    baslangic: date,
    bitis: date,
    db: Session = Depends(get_db)
):
    return TakvimService.tarih_araligi_getir(
        db,
        baslangic,
        bitis
    )