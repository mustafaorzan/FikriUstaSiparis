from datetime import date, datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.logger import logger

from app.enums.siparis_durumu import SiparisDurumu
from app.enums.siparis_turu import SiparisTuru

from app.models.musteri import Musteri
from app.models.siparis import Siparis
from app.models.yikama import Yikama
from app.models.ilaclama import Ilaclama

from app.repositories.musteri_repository import MusteriRepository
from app.repositories.siparis_repository import SiparisRepository

from app.schemas.siparis import (
    SiparisCreate,
    SiparisUpdate
)
from app.utils.hesaplama import yikama_fiyat_hesapla, ilaclama_fiyat_hesapla
from app.validators.siparis_validator import SiparisValidator
from app.validators.musteri_validator import MusteriValidator


class SiparisService:

    # ==========================================================
    # YARDIMCI METOTLAR
    # ==========================================================

    @staticmethod
    def _siparisi_getir(
        db: Session,
        siparis_id: int
    ) -> Siparis:

        siparis = SiparisRepository.id_ile_bul(
            db,
            siparis_id
        )

        if not siparis:
            logger.warning(
                f"Sipariş bulunamadı. ID={siparis_id}"
            )

            raise HTTPException(
                status_code=404,
                detail="Sipariş bulunamadı."
            )

        return siparis

    @staticmethod
    def _musteriyi_getir_veya_olustur(
        db: Session,
        ad: str,
        tel: str
    ) -> Musteri:

        musteri = MusteriRepository.telefon_ile_bul(
            db,
            tel
        )

        if musteri:
            return musteri

        logger.info(
            f"Yeni müşteri oluşturuluyor. Tel={tel}"
        )

        yeni_musteri = Musteri(
            ad=ad,
            tel=tel
        )

        return MusteriRepository.olustur(
            db,
            yeni_musteri,
            commit=False
        )

    @staticmethod
    def _siparis_turu_kontrol_et(veri):

        if (
            veri.siparis_tur == SiparisTuru.YIKAMA
            and not veri.yikama
        ):
            raise HTTPException(
                status_code=400,
                detail=(
                    "Yıkama siparişi için "
                    "yıkama bilgileri gereklidir."
                )
            )

        if (
            veri.siparis_tur == SiparisTuru.ILACLAMA
            and not veri.ilaclama
        ):
            raise HTTPException(
                status_code=400,
                detail=(
                    "İlaçlama siparişi için "
                    "ilaçlama bilgileri gereklidir."
                )
            )

    @staticmethod
    def _yikama_olustur(
        db: Session,
        siparis: Siparis,
        veri
    ) -> Yikama:

        fiyat = yikama_fiyat_hesapla(
            takim_sayi=veri.takim_sayi,
            yatak_sayi=veri.yatak_sayi,
            sandalye_sayi=veri.sandalye_sayi,
            manuel_fiyat=getattr(veri, "fiyat", None)
        )

        yikama = Yikama(
            siparis_id=siparis.id,
            takim_sayi=veri.takim_sayi,
            yatak_sayi=veri.yatak_sayi,
            sandalye_sayi=veri.sandalye_sayi,
            fiyat=fiyat
        )

        db.add(yikama)

        return yikama

    @staticmethod
    def _ilaclama_olustur(
        db: Session,
        siparis: Siparis,
        veri
    ) -> Ilaclama:

        daire_fiyat, top_fiyat = ilaclama_fiyat_hesapla(
            daire_sayi=veri.daire_sayi,
            daire_basi_fiyat=getattr(veri, "daire_basi_fiyat", None),
            manuel_toplam_fiyat=getattr(veri, "toplam_fiyat", None)
        )

        ilaclama = Ilaclama(
            siparis_id=siparis.id,
            daire_sayi=veri.daire_sayi,
            daire_basi_fiyat=daire_fiyat,
            toplam_fiyat=top_fiyat
        )

        db.add(ilaclama)

        return ilaclama

    # ==========================================================
    # SİPARİŞ OLUŞTUR
    # ==========================================================

    @staticmethod
    def siparis_olustur(
        db: Session,
        veri: SiparisCreate
    ) -> Siparis:

        try:

            # Tarih ve telefon doğrulamaları
            SiparisValidator.tarih_kontrol(veri.tarih)
            MusteriValidator.telefon_kontrol(veri.tel)

            # Sipariş türü kontrolü
            SiparisService._siparis_turu_kontrol_et(
                veri
            )

            # ----------------------------------------------
            # Müşteri
            # ----------------------------------------------

            musteri = (
                SiparisService._musteriyi_getir_veya_olustur(
                    db=db,
                    ad=veri.musteri_ad,
                    tel=veri.tel
                )
            )

            # ----------------------------------------------
            # Sipariş
            # ----------------------------------------------

            siparis = Siparis(
                musteri_id=musteri.id,
                adres=veri.adres,
                tel=veri.tel,
                siparis_tur=veri.siparis_tur.value,
                tarih=veri.tarih,
                saat=veri.saat,
                durum=SiparisDurumu.BEKLIYOR.value,
                notlar=veri.notlar
            )

            SiparisRepository.olustur(
                db,
                siparis
            )

            # Sipariş ID'sinin oluşmasını sağla
            db.flush()

            # ----------------------------------------------
            # YIKAMA
            # ----------------------------------------------

            if veri.siparis_tur == SiparisTuru.YIKAMA:

                SiparisService._yikama_olustur(
                    db=db,
                    siparis=siparis,
                    veri=veri.yikama
                )

            # ----------------------------------------------
            # İLAÇLAMA
            # ----------------------------------------------

            elif veri.siparis_tur == SiparisTuru.ILACLAMA:

                SiparisService._ilaclama_olustur(
                    db=db,
                    siparis=siparis,
                    veri=veri.ilaclama
                )

            # ----------------------------------------------
            # Kaydet
            # ----------------------------------------------

            db.commit()
            db.refresh(siparis)

            logger.info(
                f"Sipariş oluşturuldu. "
                f"ID={siparis.id} "
                f"Musteri={musteri.ad}"
            )

            return siparis

        except HTTPException:
            db.rollback()
            raise

        except Exception:

            db.rollback()

            logger.exception(
                "Sipariş oluşturulamadı."
            )

            raise

    # ==========================================================
    # SİPARİŞ LİSTELE
    # ==========================================================

    @staticmethod
    def siparis_listele(
        db: Session,
        durum: SiparisDurumu | None = None,
        siparis_tur: SiparisTuru | None = None,
        tarih: date | None = None,
        skip: int = 0,
        limit: int = 100
    ) -> list[Siparis]:

        return SiparisRepository.listele(
            db=db,
            durum=durum.value if durum else None,
            siparis_tur=siparis_tur.value if siparis_tur else None,
            tarih=tarih,
            skip=skip,
            limit=limit
        )

    # ==========================================================
    # SİPARİŞ DETAY
    # ==========================================================

    @staticmethod
    def siparis_detay(
        db: Session,
        siparis_id: int
    ) -> Siparis:

        return SiparisService._siparisi_getir(
            db,
            siparis_id
        )

    # ==========================================================
    # SİPARİŞ GÜNCELLE
    # ==========================================================

    @staticmethod
    def siparis_guncelle(
        db: Session,
        siparis_id: int,
        veri: SiparisUpdate
    ) -> Siparis:

        try:

            # ----------------------------------------------
            # Mevcut siparişi bul
            # ----------------------------------------------

            siparis = SiparisService._siparisi_getir(
                db,
                siparis_id
            )

            # ----------------------------------------------
            # Doğrulamalar
            # ----------------------------------------------
            SiparisValidator.tarih_kontrol(veri.tarih)
            MusteriValidator.telefon_kontrol(veri.tel)

            # ----------------------------------------------
            # Sipariş türü kontrolü
            # ----------------------------------------------

            SiparisService._siparis_turu_kontrol_et(
                veri
            )

            # ----------------------------------------------
            # Müşteri
            # ----------------------------------------------

            musteri = (
                SiparisService._musteriyi_getir_veya_olustur(
                    db=db,
                    ad=veri.musteri_ad,
                    tel=veri.tel
                )
            )

            # ----------------------------------------------
            # Ana sipariş bilgileri
            # ----------------------------------------------

            siparis.musteri_id = musteri.id
            siparis.adres = veri.adres
            siparis.tel = veri.tel
            siparis.siparis_tur = veri.siparis_tur.value
            siparis.tarih = veri.tarih
            siparis.saat = veri.saat
            siparis.notlar = veri.notlar

            # ----------------------------------------------
            # YIKAMA
            # ----------------------------------------------

            if veri.siparis_tur == SiparisTuru.YIKAMA:

                # İlaçlama detayını kaldır
                if siparis.ilaclama:

                    db.delete(
                        siparis.ilaclama
                    )

                    siparis.ilaclama = None

                # Mevcut yıkamayı güncelle
                if siparis.yikama:

                    siparis.yikama.takim_sayi = (
                        veri.yikama.takim_sayi
                    )

                    siparis.yikama.yatak_sayi = (
                        veri.yikama.yatak_sayi
                    )

                    siparis.yikama.sandalye_sayi = (
                        veri.yikama.sandalye_sayi
                    )

                    siparis.yikama.fiyat = yikama_fiyat_hesapla(
                        takim_sayi=veri.yikama.takim_sayi,
                        yatak_sayi=veri.yikama.yatak_sayi,
                        sandalye_sayi=veri.yikama.sandalye_sayi,
                        manuel_fiyat=getattr(veri.yikama, "fiyat", None)
                    )

                # Yıkama yoksa oluştur
                else:

                    SiparisService._yikama_olustur(
                        db=db,
                        siparis=siparis,
                        veri=veri.yikama
                    )

            # ----------------------------------------------
            # İLAÇLAMA
            # ----------------------------------------------

            elif veri.siparis_tur == SiparisTuru.ILACLAMA:

                # Yıkama detayını kaldır
                if siparis.yikama:

                    db.delete(
                        siparis.yikama
                    )

                    siparis.yikama = None

                # Mevcut ilaçlamayı güncelle
                if siparis.ilaclama:

                    daire_fiyat, top_fiyat = ilaclama_fiyat_hesapla(
                        daire_sayi=veri.ilaclama.daire_sayi,
                        daire_basi_fiyat=getattr(veri.ilaclama, "daire_basi_fiyat", None),
                        manuel_toplam_fiyat=getattr(veri.ilaclama, "toplam_fiyat", None)
                    )

                    siparis.ilaclama.daire_sayi = (
                        veri.ilaclama.daire_sayi
                    )
                    siparis.ilaclama.daire_basi_fiyat = daire_fiyat
                    siparis.ilaclama.toplam_fiyat = top_fiyat

                # İlaçlama yoksa oluştur
                else:

                    SiparisService._ilaclama_olustur(
                        db=db,
                        siparis=siparis,
                        veri=veri.ilaclama
                    )

            # ----------------------------------------------
            # Kaydet
            # ----------------------------------------------

            db.commit()
            db.refresh(siparis)

            logger.info(
                f"Sipariş güncellendi. "
                f"ID={siparis.id}"
            )

            return siparis

        except HTTPException:
            db.rollback()
            raise

        except Exception:

            db.rollback()

            logger.exception(
                f"Sipariş güncellenemedi. "
                f"ID={siparis_id}"
            )

            raise

    # ==========================================================
    # SİPARİŞ SİL
    # ==========================================================

    @staticmethod
    def siparis_sil(
        db: Session,
        siparis_id: int
    ):

        try:

            siparis = SiparisService._siparisi_getir(
                db,
                siparis_id
            )

            SiparisRepository.sil(
                db,
                siparis
            )

            db.commit()

            logger.info(
                f"Sipariş silindi. ID={siparis_id}"
            )

            return {
                "message": "Sipariş başarıyla silindi."
            }

        except HTTPException:
            db.rollback()
            raise

        except Exception:

            db.rollback()

            logger.exception(
                f"Sipariş silinemedi. "
                f"ID={siparis_id}"
            )

            raise

    # ==========================================================
    # DURUM GÜNCELLE
    # ==========================================================

    @staticmethod
    def durum_guncelle(
        db: Session,
        siparis_id: int,
        veri
    ) -> Siparis:

        try:

            siparis = SiparisService._siparisi_getir(
                db,
                siparis_id
            )

            # ----------------------------------------------
            # Durumu güncelle
            # ----------------------------------------------

            siparis.durum = veri.durum.value

            # ----------------------------------------------
            # Sipariş tamamlandıysa tamamlanma tarihini yaz
            # ----------------------------------------------

            if veri.durum == SiparisDurumu.TAMAMLANDI:

                siparis.tamamlanan_tarih = datetime.now()

            else:

                siparis.tamamlanan_tarih = None

            # ----------------------------------------------
            # Kaydet
            # ----------------------------------------------

            db.commit()
            db.refresh(siparis)

            logger.info(
                f"Sipariş durumu güncellendi. "
                f"ID={siparis.id} "
                f"Durum={siparis.durum}"
            )

            return siparis

        except HTTPException:
            db.rollback()
            raise

        except Exception:

            db.rollback()

            logger.exception(
                f"Sipariş durumu güncellenemedi. "
                f"ID={siparis_id}"
            )

            raise