from sqlalchemy import Column, Integer, Numeric, String, Float, ForeignKey, Integer
from app.database import Base
from sqlalchemy.orm import relationship

class Yikama(Base):
    __tablename__ = "yikama"

    id = Column(Integer, primary_key=True, index=True)

    siparis_id = Column(Integer, ForeignKey("siparis.id"))

    takim_sayi = Column(Integer, default=0)

    yatak_sayi = Column(Integer, default=0)

    sandalye_sayi = Column(Integer, default=0)

    fiyat = Column(Numeric(10, 2))

    siparis = relationship("Siparis",
                           back_populates="yikama")