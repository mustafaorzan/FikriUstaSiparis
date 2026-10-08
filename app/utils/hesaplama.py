# ==========================================================
# Fikri Usta Sipariş Sistemi - Fiyat Hesaplama Modülü
# ==========================================================

# Varsayılan Hizmet Birim Fiyatları (TL)
VARSAYILAN_TAKIM_FIYAT: float = 750.0
VARSAYILAN_YATAK_FIYAT: float = 400.0
VARSAYILAN_SANDALYE_FIYAT: float = 75.0
VARSAYILAN_DAIRE_ILACLAMA_FIYAT: float = 500.0


def yikama_fiyat_hesapla(
    takim_sayi: int = 0,
    yatak_sayi: int = 0,
    sandalye_sayi: int = 0,
    manuel_fiyat: float | None = None
) -> float:
    """
    Yıkama siparişi için toplam fiyatı hesaplar.
    Kullanıcı manuel özel bir fiyat girdiyse o fiyatı esas alır,
    aksi takdirde birim fiyatlar üzerinden otomatik hesaplar.
    """
    if manuel_fiyat is not None and manuel_fiyat >= 0:
        return round(float(manuel_fiyat), 2)

    toplam = (
        (takim_sayi or 0) * VARSAYILAN_TAKIM_FIYAT
        + (yatak_sayi or 0) * VARSAYILAN_YATAK_FIYAT
        + (sandalye_sayi or 0) * VARSAYILAN_SANDALYE_FIYAT
    )

    return round(float(toplam), 2)


def ilaclama_fiyat_hesapla(
    daire_sayi: int = 1,
    daire_basi_fiyat: float | None = None,
    manuel_toplam_fiyat: float | None = None
) -> tuple[float, float]:
    """
    İlaçlama siparişi için (daire_basi_fiyat, toplam_fiyat) ikilisini döndürür.
    Kullanıcı özel toplam fiyat girdiyse onu esas alır.
    """
    birim_fiyat = (
        float(daire_basi_fiyat)
        if daire_basi_fiyat is not None and daire_basi_fiyat >= 0
        else VARSAYILAN_DAIRE_ILACLAMA_FIYAT
    )

    daire = max(1, daire_sayi or 1)

    if manuel_toplam_fiyat is not None and manuel_toplam_fiyat >= 0:
        return round(birim_fiyat, 2), round(float(manuel_toplam_fiyat), 2)

    toplam = daire * birim_fiyat
    return round(birim_fiyat, 2), round(float(toplam), 2)
