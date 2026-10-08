from pydantic import BaseModel, Field


class MusteriCreate(BaseModel):
    ad: str = Field(..., max_length=100)
    tel: str = Field(pattern=r"^[0-9]{10,11}$")


class MusteriUpdate(BaseModel):
    ad: str = Field(..., max_length=100)
    tel: str = Field(pattern=r"^[0-9]{10,11}$")


class MusteriResponse(BaseModel):
    id: int
    ad: str
    tel: str

    class Config:
        from_attributes = True