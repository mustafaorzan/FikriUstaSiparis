import re

from fastapi import HTTPException


class MusteriValidator:

    @staticmethod
    def telefon_kontrol(tel: str):

        if not re.fullmatch(r"^[0-9]{10,11}$", tel):
            raise HTTPException(
                status_code=400,
                detail="Geçerli bir telefon numarası giriniz."
            )