from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.musteri import Musteri
from app.repositories.musteri_repository import MusteriRepository
from app.repositories.siparis_repository import SiparisRepository
from app.schemas.musteri import MusteriCreate, MusteriUpdate
from app.validators.musteri_validator import MusteriValidator


class MusteriService:

    @staticmethod
    def olustur(db: Session, musteri: MusteriCreate):
        MusteriValidator.telefon_kontrol(musteri.tel)

        mevcut_musteri = MusteriRepository.telefon_ile_bul(
            db,
            musteri.tel
        )

        if mevcut_musteri:
            raise HTTPException(
                status_code=400,
                detail="Bu telefon numarasına ait müşteri zaten mevcut."
            )

        yeni_musteri = Musteri(
            ad=musteri.ad,
            tel=musteri.tel
        )

        return MusteriRepository.olustur(
            db,
            yeni_musteri
        )

    @staticmethod
    def tumunu_getir(db: Session):
        return MusteriRepository.tumunu_getir(db)

    @staticmethod
    def id_ile_getir(db: Session, musteri_id: int):
        musteri = MusteriRepository.id_ile_bul(
            db,
            musteri_id
        )

        if musteri is None:
            raise HTTPException(
                status_code=404,
                detail="Müşteri bulunamadı."
            )

        return musteri

    @staticmethod
    def ara(db: Session, q: str):
        return MusteriRepository.ara(
            db,
            q
        )

    @staticmethod
    def siparis_gecmisi(db: Session, musteri_id: int):
        MusteriService.id_ile_getir(
            db,
            musteri_id
        )

        return SiparisRepository.musteri_siparisleri(
            db,
            musteri_id
        )

    @staticmethod
    def guncelle(
        db: Session,
        musteri_id: int,
        veri: MusteriUpdate
    ):
        MusteriValidator.telefon_kontrol(veri.tel)

        musteri = MusteriService.id_ile_getir(
            db,
            musteri_id
        )

        # Telefon numarası değiştiriliyorsa
        # başka müşteride kullanılıyor mu kontrol et
        if veri.tel != musteri.tel:
            mevcut_musteri = MusteriRepository.telefon_ile_bul(
                db,
                veri.tel
            )

            if mevcut_musteri and mevcut_musteri.id != musteri_id:
                raise HTTPException(
                    status_code=400,
                    detail="Bu telefon numarasına ait başka bir müşteri zaten mevcut."
                )

        musteri.ad = veri.ad
        musteri.tel = veri.tel

        return MusteriRepository.kaydet(
            db,
            musteri
        )

    @staticmethod
    def sil(db: Session, musteri_id: int):
        musteri = MusteriService.id_ile_getir(
            db,
            musteri_id
        )

        # Siparişi olan müşteriyi silme.
        # Çünkü Musteri modelindeki cascade ayarı
        # müşterinin siparişlerini de silebilir.
        if musteri.siparisler:
            raise HTTPException(
                status_code=400,
                detail="Siparişi bulunan müşteri silinemez."
            )

        MusteriRepository.sil(
            db,
            musteri
        )

        return {
            "message": "Müşteri başarıyla silindi."
        }