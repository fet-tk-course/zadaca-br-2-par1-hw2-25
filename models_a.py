from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator
# TODO: Student A - Definiši svoj SQLModel entitet ovdje
# 

#Glavni model 
class Instrument(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    inventory_number: str
    manufacturer: str
    purchase_year: int
    price: float
    is_available: bool
    location: Optional[str] = None

#Shema za kreiranje novog instrumenta
class InstrumentCreate(SQLModel):
    name: str
    inventory_number: str
    manufacturer: str
    purchase_year: int
    price: float
    is_available: bool
    location: Optional[str] = None
#Dodani validatori za provjeru ispravnog unosa godine (godina ne smije biti negativna) i provjera unosa cijene (cijena mora biti pozitivna)
    @field_validator("purchase_year")
    @classmethod
    def validate_purchase_year(cls, v):
        if v < 0:
            raise ValueError("Godina kupovine ne može biti negativna.")
        return v
    
    @field_validator('price')
    @classmethod
    def price_mora_biti_pozitivna(cls, v):
        if v <= 0:
            raise ValueError('Cijena mora biti veća od nule')
        return v
    
#Shema za djelimicno azuriranje instrumenta
class InstrumentUpdate(SQLModel):
    name: Optional[str] = None
    inventory_number: Optional[str] = None
    manufacturer: Optional[str] = None
    purchase_year: Optional[int] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None
    location: Optional[str] = None

    

