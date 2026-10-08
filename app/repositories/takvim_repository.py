from datetime import date, timedelta

from sqlalchemy.orm import Session, joinedload

from app.models.siparis import Siparis


class TakvimRepository:

    @staticmethod
    def haftalik_getir(
        db: Session,
        baslangic: date | None = None
    ):
        """
        Haftalık siparişleri getir.
        Parametre verilmezse içinde bulunulan haftayı getirir.
        """

        if baslangic is None:
            bugun = date.today()
            baslangic = bugun - timedelta(days=bugun.weekday())

        bitis = baslangic + timedelta(days=6)

        return (
            db.query(Siparis)
            .options(joinedload(Siparis.musteri))
            .filter(
                Siparis.tarih >= baslangic,
                Siparis.tarih <= bitis
            )
            .order_by(
                Siparis.tarih,
                Siparis.saat
            )
            .all()
        )

    @staticmethod
    def gunluk_getir(
        db: Session,
        tarih: date
    ):
        """
        Belirli bir güne ait siparişleri getir.
        """

        return (
            db.query(Siparis)
            .options(joinedload(Siparis.musteri))
            .filter(Siparis.tarih == tarih)
            .order_by(Siparis.saat)
            .all()
        )

    @staticmethod
    def bugunku_getir(
        db: Session
    ):
        """
        Bugünkü siparişleri getir.
        """

        return (
            db.query(Siparis)
            .options(joinedload(Siparis.musteri))
            .filter(Siparis.tarih == date.today())
            .order_by(Siparis.saat)
            .all()
        )

    @staticmethod
    def tarih_araligi_getir(
        db: Session,
        baslangic: date,
        bitis: date
    ):
        """
        Başlangıç ve bitiş tarihi arasındaki siparişleri getir.
        """

        return (
            db.query(Siparis)
            .options(joinedload(Siparis.musteri))
            .filter(
                Siparis.tarih >= baslangic,
                Siparis.tarih <= bitis
            )
            .order_by(
                Siparis.tarih,
                Siparis.saat
            )
            .all()
        )