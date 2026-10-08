from pydantic import BaseModel
from datetime import date, datetime


class MusteriDetayResponse(BaseModel):
    id: int
    ad: str
    tel: str

    class Config:
        from_attributes = True

class YikamaDetayResponse(BaseModel):
    takim_sayi: int
    yatak_sayi: int
    sandalye_sayi: int
    fiyat: float | None = None

    class Config:
        from_attributes = True

class IlaclamaDetayResponse(BaseModel):
    daire_sayi: int
    daire_basi_fiyat: float | None = None
    toplam_fiyat: float | None = None

    class Config:
        from_attributes = True


class SiparisDetayResponse(BaseModel):

    id: int

    musteri: MusteriDetayResponse

    adres: str

    siparis_tur: str

    tarih: date

    saat: str

    durum: str

    tamamlanan_tarih: datetime | None

    notlar: str | None

    yikama: YikamaDetayResponse | None

    ilaclama: IlaclamaDetayResponse | None

    class Config:
        from_attributes = True