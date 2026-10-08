from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Musteri(Base):
    __tablename__ = "musteri"

    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String)
    tel = Column(String)

    siparisler = relationship(
        "Siparis",
        back_populates="musteri",
        cascade="all, delete-orphan"
    )