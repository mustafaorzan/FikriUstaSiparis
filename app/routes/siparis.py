from datetime import date
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.siparis import (
    SiparisCreate,
    SiparisUpdate
)

from app.schemas.siparis_detay import SiparisDetayResponse
from app.services.siparis_service import SiparisService
from app.schemas.durum import DurumGuncelleRequest
from app.enums.siparis_durumu import SiparisDurumu
from app.enums.siparis_turu import SiparisTuru


router = APIRouter(
    prefix="/siparis",
    tags=["Sipariş"]
)


# -------------------------
# Siparişleri Listele
# -------------------------
@router.get(
    "",
    response_model=list[SiparisDetayResponse]
)
def siparis_listele(
    durum: SiparisDurumu | None = None,
    siparis_tur: SiparisTuru | None = None,
    tarih: date | None = None,
    skip: int = Query(0, ge=0, description="Atlanacak kayıt sayısı"),
    limit: int = Query(100, ge=1, le=500, description="Döndürülecek maksimum kayıt sayısı"),
    db: Session = Depends(get_db)
):
    return SiparisService.siparis_listele(
        db=db,
        durum=durum,
        siparis_tur=siparis_tur,
        tarih=tarih,
        skip=skip,
        limit=limit
    )


# -------------------------
# Yeni Sipariş Oluştur
# -------------------------
@router.post(
    "",
    response_model=SiparisDetayResponse,
    status_code=201
)
def siparis_olustur(
    veri: SiparisCreate,
    db: Session = Depends(get_db)
):

    return SiparisService.siparis_olustur(
        db,
        veri
    )


# -------------------------
# Sipariş Detayı
# -------------------------
@router.get(
    "/{siparis_id}",
    response_model=SiparisDetayResponse
)
def siparis_detay(
    siparis_id: int,
    db: Session = Depends(get_db)
):

    return SiparisService.siparis_detay(
        db,
        siparis_id
    )


# -------------------------
# Sipariş Güncelle
# -------------------------
@router.put(
    "/{siparis_id}",
    response_model=SiparisDetayResponse
)
def siparis_guncelle(
    siparis_id: int,
    veri: SiparisUpdate,
    db: Session = Depends(get_db)
):

    return SiparisService.siparis_guncelle(
        db,
        siparis_id,
        veri
    )


# -------------------------
# Sipariş Sil
# -------------------------
@router.delete(
    "/{siparis_id}"
)
def siparis_sil(
    siparis_id: int,
    db: Session = Depends(get_db)
):

    return SiparisService.siparis_sil(
        db,
        siparis_id
    )

@router.patch(
    "/{siparis_id}/durum",
    response_model=SiparisDetayResponse
)
def durum_guncelle(
    siparis_id: int,
    veri: DurumGuncelleRequest,
    db: Session = Depends(get_db)
):

    return SiparisService.durum_guncelle(
        db,
        siparis_id,
        veri
    )