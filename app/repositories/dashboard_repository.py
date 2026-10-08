from datetime import date, timedelta

from sqlalchemy import func, case, and_
from sqlalchemy.orm import Session

from app.models.siparis import Siparis
from app.enums.siparis_durumu import SiparisDurumu


class DashboardRepository:

    @staticmethod
    def bugunku_toplam(db: Session) -> int:

        return (
            db.query(func.count(Siparis.id))
            .filter(Siparis.tarih == date.today())
            .scalar() or 0
        )

    @staticmethod
    def haftalik_toplam(db: Session) -> int:

        bugun = date.today()

        hafta_baslangic = bugun - timedelta(days=bugun.weekday())
        hafta_bitis = hafta_baslangic + timedelta(days=6)

        return (
            db.query(func.count(Siparis.id))
            .filter(
                Siparis.tarih >= hafta_baslangic,
                Siparis.tarih <= hafta_bitis
            )
            .scalar() or 0
        )

    @staticmethod
    def durum_sayisi(
        db: Session,
        durum: str
    ) -> int:

        return (
            db.query(func.count(Siparis.id))
            .filter(Siparis.durum == durum)
            .scalar() or 0
        )

    @staticmethod
    def tum_istatistikleri_getir(db: Session) -> dict:
        bugun = date.today()
        hafta_baslangic = bugun - timedelta(days=bugun.weekday())
        hafta_bitis = hafta_baslangic + timedelta(days=6)

        result = (
            db.query(
                func.count(case((Siparis.tarih == bugun, Siparis.id), else_=None)).label("bugun_toplam"),
                func.count(case((and_(Siparis.tarih >= hafta_baslangic, Siparis.tarih <= hafta_bitis), Siparis.id), else_=None)).label("haftalik_toplam"),
                func.count(case((Siparis.durum == SiparisDurumu.BEKLIYOR.value, Siparis.id), else_=None)).label("bekleyen"),
                func.count(case((Siparis.durum == SiparisDurumu.ONAYLANDI.value, Siparis.id), else_=None)).label("onaylandi"),
                func.count(case((Siparis.durum == SiparisDurumu.YOLA_CIKILDI.value, Siparis.id), else_=None)).label("yola_cikildi"),
                func.count(case((Siparis.durum == SiparisDurumu.ISLEMDE.value, Siparis.id), else_=None)).label("islemde"),
                func.count(case((Siparis.durum == SiparisDurumu.TAMAMLANDI.value, Siparis.id), else_=None)).label("tamamlandi"),
                func.count(case((Siparis.durum == SiparisDurumu.IPTAL.value, Siparis.id), else_=None)).label("iptal"),
            )
            .first()
        )

        return {
            "bugun_toplam": (getattr(result, "bugun_toplam", 0) or 0) if result else 0,
            "bekleyen": (getattr(result, "bekleyen", 0) or 0) if result else 0,
            "onaylandi": (getattr(result, "onaylandi", 0) or 0) if result else 0,
            "yola_cikildi": (getattr(result, "yola_cikildi", 0) or 0) if result else 0,
            "islemde": (getattr(result, "islemde", 0) or 0) if result else 0,
            "tamamlandi": (getattr(result, "tamamlandi", 0) or 0) if result else 0,
            "iptal": (getattr(result, "iptal", 0) or 0) if result else 0,
            "haftalik_toplam": (getattr(result, "haftalik_toplam", 0) or 0) if result else 0,
        }