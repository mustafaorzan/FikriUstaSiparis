from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.musteri import MusteriCreate, MusteriUpdate, MusteriResponse
from app.schemas.musteri_siparis import MusteriSiparisResponse
from app.services.musteri_service import MusteriService


router = APIRouter(
    prefix="/musteri",
    tags=["Müşteri"]
)


@router.post(
    "",
    response_model=MusteriResponse,
    status_code=201
)
def musteri_olustur(
    musteri: MusteriCreate,
    db: Session = Depends(get_db)
):
    return MusteriService.olustur(
        db,
        musteri
    )


@router.get(
    "/ara",
    response_model=list[MusteriResponse]
)
def musteri_ara(
    q: str = Query(
        ...,
        min_length=1,
        description="Ad veya telefon ile arama"
    ),
    db: Session = Depends(get_db)
):
    return MusteriService.ara(
        db,
        q
    )


@router.get(
    "",
    response_model=list[MusteriResponse]
)
def tum_musteriler(
    db: Session = Depends(get_db)
):
    return MusteriService.tumunu_getir(db)


@router.get(
    "/{musteri_id}",
    response_model=MusteriResponse
)
def musteri_getir(
    musteri_id: int,
    db: Session = Depends(get_db)
):
    return MusteriService.id_ile_getir(
        db,
        musteri_id
    )


@router.get(
    "/{musteri_id}/siparisler",
    response_model=list[MusteriSiparisResponse]
)
def musteri_siparisleri(
    musteri_id: int,
    db: Session = Depends(get_db)
):
    return MusteriService.siparis_gecmisi(
        db,
        musteri_id
    )


@router.put(
    "/{musteri_id}",
    response_model=MusteriResponse
)
def musteri_guncelle(
    musteri_id: int,
    veri: MusteriUpdate,
    db: Session = Depends(get_db)
):
    return MusteriService.guncelle(
        db,
        musteri_id,
        veri
    )


@router.delete(
    "/{musteri_id}"
)
def musteri_sil(
    musteri_id: int,
    db: Session = Depends(get_db)
):
    return MusteriService.sil(
        db,
        musteri_id
    )