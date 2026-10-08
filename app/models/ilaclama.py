from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class Ilaclama(Base):
    __tablename__ = "ilaclama"

    id = Column(Integer, primary_key=True, index=True)

    siparis_id = Column(Integer, ForeignKey("siparis.id"))

    daire_sayi = Column(Integer, default=1)

    daire_basi_fiyat = Column(Numeric(10, 2))

    toplam_fiyat = Column(Numeric(10, 2))

    siparis = relationship("Siparis",
                            back_populates="ilaclama")