from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Siparis(Base):
    __tablename__ = "siparis"

    id = Column(Integer, primary_key=True, index=True)

    musteri_id = Column(
        Integer,
        ForeignKey("musteri.id"),
        nullable=False)

    adres = Column(Text)

    tel = Column(String)

    siparis_tur = Column(String)

    tarih = Column(Date)

    saat = Column(String)

    durum = Column(String, default="BEKLİYOR")

    notlar = Column(String)

    alinan_tarih = Column(DateTime,
                        server_default=func.now())

    tamamlanan_tarih = Column(DateTime)

    # İlişki
    musteri = relationship(
        "Musteri",
        back_populates="siparisler")
    
    ilaclama = relationship(
        "Ilaclama",
        back_populates="siparis",
        uselist=False,
        cascade="all, delete-orphan"
    )

    yikama = relationship(
        "Yikama",
        back_populates="siparis",
        uselist=False,
        cascade="all, delete-orphan"
    )
    