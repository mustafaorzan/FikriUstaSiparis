from pydantic import BaseModel

class DashboardResponse(BaseModel):

    bugun_toplam: int
    bekleyen: int
    onaylandi: int
    yola_cikildi: int
    islemde: int
    tamamlandi: int
    iptal: int
    haftalik_toplam: int