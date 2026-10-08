from sqlalchemy.orm import Session
from app.models.ilaclama import Ilaclama


class IlaclamaRepository:

    @staticmethod
    def olustur(db: Session, ilaclama: Ilaclama):
        db.add(ilaclama)