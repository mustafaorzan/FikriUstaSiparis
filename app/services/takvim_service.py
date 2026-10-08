from datetime import date

from sqlalchemy.orm import Session

from app.constants.takvim import TAKVIM_RENKLERI
from app.repositories.takvim_repository import TakvimRepository
from app.schemas.takvim import TakvimItemResponse


class TakvimService:

    @staticmethod
    def _takvim_item_olustur(siparis):

        return TakvimItemResponse(
            id=siparis.id,
            tarih=siparis.tarih,
            saat=siparis.saat,
            musteri=siparis.musteri.ad if siparis.musteri else "Bilinmeyen Müşteri",
            adres=siparis.adres,
            siparis_tur=siparis.siparis_tur,
            durum=siparis.durum,
            renk=TAKVIM_RENKLERI.get(
                siparis.durum,
                "#95a5a6"
            )
        )

    @staticmethod
    def haftalik_getir(
        db: Session,
        baslangic: date | None = None
    ):

        siparisler = TakvimRepository.haftalik_getir(
            db,
            baslangic
        )

        return [
            TakvimService._takvim_item_olustur(s)
            for s in siparisler
        ]

    @staticmethod
    def gunluk_getir(
        db: Session,
        tarih: date
    ):

        siparisler = TakvimRepository.gunluk_getir(
            db,
            tarih
        )

        return [
            TakvimService._takvim_item_olustur(s)
            for s in siparisler
        ]

    @staticmethod
    def bugunku_getir(
        db: Session
    ):

        siparisler = TakvimRepository.bugunku_getir(db)

        return [
            TakvimService._takvim_item_olustur(s)
            for s in siparisler
        ]

    @staticmethod
    def tarih_araligi_getir(
        db: Session,
        baslangic: date,
        bitis: date
    ):

        siparisler = TakvimRepository.tarih_araligi_getir(
            db,
            baslangic,
            bitis
        )

        return [
            TakvimService._takvim_item_olustur(s)
            for s in siparisler
        ]