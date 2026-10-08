from datetime import date

from fastapi import HTTPException


class SiparisValidator:

    @staticmethod
    def tarih_kontrol(tarih: date):

        if tarih < date.today():
            raise HTTPException(
                status_code=400,
                detail="Geçmiş tarihe sipariş oluşturulamaz."
            )