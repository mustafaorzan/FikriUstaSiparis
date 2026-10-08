from pydantic import BaseModel


class YikamaCreate(BaseModel):
    takim_sayi: int = 0
    yatak_sayi: int = 0
    sandalye_sayi: int = 0
    fiyat: float | None = None