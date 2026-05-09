from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from database import get_session
from models_a import Instrument, InstrumentCreate, InstrumentUpdate


router = APIRouter(prefix="/instruments", tags=["Instruments"])

#GET /instruments - Dohvati sve instrumente  po dostupnosti
@router.get("/", response_model=list[Instrument])
def get_instruments(is_available: bool | None = Query(default=None), session: Session = Depends(get_session)):
    query = select(Instrument)
    if is_available is not None:
        query = query.where(Instrument.is_available == is_available)
    instruments = session.exec(query).all()
    return instruments
