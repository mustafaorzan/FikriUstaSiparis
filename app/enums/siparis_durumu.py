from enum import Enum


class SiparisDurumu(str, Enum):
    BEKLIYOR = "BEKLİYOR"
    ONAYLANDI = "ONAYLANDI"
    YOLA_CIKILDI = "YOLA_CIKILDI"
    ISLEMDE = "ISLEMDE"
    TAMAMLANDI = "TAMAMLANDI"
    IPTAL = "IPTAL"