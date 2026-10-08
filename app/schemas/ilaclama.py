from pydantic import BaseModel


class IlaclamaCreate(BaseModel):
    daire_sayi: int = 1
    daire_basi_fiyat: float | None = None
    toplam_fiyat: float | None = None