from pydantic import BaseModel, Field

from typing import Optional
from datetime import date

from app.schemas.yikama import YikamaCreate
from app.schemas.ilaclama import IlaclamaCreate
from app.enums.siparis_turu import SiparisTuru


class SiparisCreate(BaseModel):

    musteri_ad: str = Field(..., max_length=100)
    adres: str
    tel: str = Field(..., pattern=r"^[0-9]{10,11}$")
    siparis_tur: SiparisTuru
    tarih: date
    saat: str
    
    notlar: Optional[str] = None

    yikama: Optional[YikamaCreate] = None
    ilaclama: Optional[IlaclamaCreate] = None

class SiparisResponse(BaseModel):
    id: int
    musteri_id: int
    adres: str
    siparis_tur: str
    tarih: date
    saat: str
    durum: str
    notlar: Optional[str]

    class Config:
        from_attributes = True

class SiparisUpdate(BaseModel):
    musteri_ad: str = Field(..., max_length=100)
    adres: str
    tel: str = Field(..., pattern=r"^[0-9]{10,11}$")

    siparis_tur: SiparisTuru

    tarih: date
    saat: str

    notlar: str | None = None

    yikama: YikamaCreate | None = None
    ilaclama: IlaclamaCreate | None = None