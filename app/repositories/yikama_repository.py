from sqlalchemy.orm import Session
from app.models.yikama import Yikama


class YikamaRepository:

    @staticmethod
    def olustur(db: Session, yikama: Yikama):
        db.add(yikama)