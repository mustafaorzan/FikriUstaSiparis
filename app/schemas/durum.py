from pydantic import BaseModel
from app.enums.siparis_durumu import SiparisDurumu

class DurumGuncelleRequest(BaseModel):
    durum: SiparisDurumu