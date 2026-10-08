from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.musteri import Musteri


class MusteriRepository:

    @staticmethod
    def telefon_ile_bul(
        db: Session,
        telefon: str
    ):
        return (
            db.query(Musteri)
            .filter(Musteri.tel == telefon)
            .first()
        )

    @staticmethod
    def id_ile_bul(
        db: Session,
        musteri_id: int
    ):
        return (
            db.query(Musteri)
            .filter(Musteri.id == musteri_id)
            .first()
        )

    @staticmethod
    def tumunu_getir(
        db: Session
    ):
        return (
            db.query(Musteri)
            .order_by(Musteri.ad)
            .all()
        )

    @staticmethod
    def ara(
        db: Session,
        q: str
    ):
        return (
            db.query(Musteri)
            .filter(
                or_(
                    Musteri.ad.ilike(f"%{q}%"),
                    Musteri.tel.ilike(f"%{q}%")
                )
            )
            .order_by(Musteri.ad)
            .all()
        )

    @staticmethod
    def olustur(
        db: Session,
        musteri: Musteri,
        commit: bool = True
    ):
        db.add(musteri)
        if commit:
            db.commit()
            db.refresh(musteri)
        else:
            db.flush()

        return musteri

    @staticmethod
    def kaydet(
        db: Session,
        musteri: Musteri
    ):
        db.add(musteri)
        db.commit()
        db.refresh(musteri)

        return musteri

    @staticmethod
    def sil(
        db: Session,
        musteri: Musteri
    ):
        db.delete(musteri)
        db.commit()