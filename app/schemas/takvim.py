from datetime import date
from pydantic import BaseModel

from app.enums.siparis_durumu import SiparisDurumu
from app.enums.siparis_turu import SiparisTuru


class TakvimItemResponse(BaseModel):
    id: int
    tarih: date
    saat: str
    musteri: str
    adres: str
    siparis_tur: SiparisTuru
    durum: SiparisDurumu
    renk: str