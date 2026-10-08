from datetime import date
from sqlalchemy.orm import Session, joinedload

from app.models.siparis import Siparis


class SiparisRepository:

    @staticmethod
    def olustur(db: Session, siparis: Siparis):
        db.add(siparis)

    @staticmethod
    def listele(
        db: Session,
        durum: str | None = None,
        siparis_tur: str | None = None,
        tarih: date | None = None,
        skip: int = 0,
        limit: int = 100
    ):
        query = (
            db.query(Siparis)
            .options(
                joinedload(Siparis.musteri),
                joinedload(Siparis.yikama),
                joinedload(Siparis.ilaclama)
            )
        )

        if durum:
            query = query.filter(Siparis.durum == durum)

        if siparis_tur:
            query = query.filter(Siparis.siparis_tur == siparis_tur)

        if tarih:
            query = query.filter(Siparis.tarih == tarih)

        return (
            query
            .order_by(
                Siparis.tarih.desc(),
                Siparis.saat.desc()
            )
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    @staticmethod
    def sil(db: Session, siparis: Siparis):
        db.delete(siparis)

    @staticmethod
    def id_ile_bul(
        db: Session,
        siparis_id: int
    ):
        return (
            db.query(Siparis)
            .options(
                joinedload(Siparis.musteri),
                joinedload(Siparis.yikama),
                joinedload(Siparis.ilaclama)
            )
            .filter(Siparis.id == siparis_id)
            .first()
        )
    
    @staticmethod
    def kaydet(db: Session, siparis: Siparis)-> Siparis:

        db.add(siparis)
        db.commit()
        db.refresh(siparis)

        return siparis
    
    @staticmethod
    def musteri_siparisleri(
        db: Session,
        musteri_id: int
    ):

        return (
            db.query(Siparis)
            .filter(
                Siparis.musteri_id == musteri_id
            )
            .order_by(
                Siparis.tarih.desc(),
                Siparis.saat.desc()
            )
            .all()
        )