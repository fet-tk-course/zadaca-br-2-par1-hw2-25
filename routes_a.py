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

#GET /instruments/"{id} - dohvatanje instrumenta po id-u"
@router.get("/{id}", response_model=Instrument)
def get_instrument(id: int, session: Session = Depends(get_session)):
    instrument = session.get(Instrument, id)
    if not instrument:
        raise HTTPException(status_code=404, detail="Instrument nije pronađen")
    return instrument

#POST /instruments - kreiranje novog instrumenta
@router.post("/", response_model=Instrument, status_code=201)
def create_instrument(instrument_create: InstrumentCreate, session: Session = Depends(get_session)):
    instrument = Instrument.from_orm(instrument_create)
    session.add(instrument)
    session.commit()
    session.refresh(instrument)
    return instrument

