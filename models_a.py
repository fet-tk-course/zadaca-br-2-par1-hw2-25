from sqlmodel import SQLModel, Field
from typing import Optional

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

#Shema za djelimicno azuriranje instrumenta
class InstrumentUpdate(SQLModel):
    name: Optional[str] = None
    inventory_number: Optional[str] = None
    manufacturer: Optional[str] = None
    purchase_year: Optional[int] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None
    location: Optional[str] = None

    

