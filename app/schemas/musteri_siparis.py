from datetime import date
from pydantic import BaseModel

from app.enums.siparis_durumu import SiparisDurumu
from app.enums.siparis_turu import SiparisTuru


class MusteriSiparisResponse(BaseModel):
    id: int

    tarih: date

    saat: str

    siparis_tur: SiparisTuru

    durum: SiparisDurumu

    class Config:
        from_attributes = True