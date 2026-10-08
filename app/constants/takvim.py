from app.enums.siparis_durumu import SiparisDurumu

TAKVIM_RENKLERI = {
    # String değerleri (veritabanından gelen durum string'leri için)
    SiparisDurumu.BEKLIYOR.value: "#f39c12",
    SiparisDurumu.ONAYLANDI.value: "#3498db",
    SiparisDurumu.YOLA_CIKILDI.value: "#8e44ad",
    SiparisDurumu.ISLEMDE.value: "#16a085",
    SiparisDurumu.TAMAMLANDI.value: "#27ae60",
    SiparisDurumu.IPTAL.value: "#e74c3c",

    # Enum üyeleri
    SiparisDurumu.BEKLIYOR: "#f39c12",
    SiparisDurumu.ONAYLANDI: "#3498db",
    SiparisDurumu.YOLA_CIKILDI: "#8e44ad",
    SiparisDurumu.ISLEMDE: "#16a085",
    SiparisDurumu.TAMAMLANDI: "#27ae60",
    SiparisDurumu.IPTAL: "#e74c3c",
}