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

#GET /instruments/count - dohvati broj dostupnih instrumenata
@router.get("/count")
def count_instruments(session: Session = Depends(get_session)):
    count = session.exec(select(Instrument)).all()
    count_available = [i for i in count if i.is_available]
    return {"dostupno": len(count_available)}

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
    existing_instrument = session.exec(select(Instrument).where(Instrument.inventory_number == instrument_create.inventory_number)).first()
    if existing_instrument:
        raise HTTPException(status_code=409, detail="Instrument sa istim inventarnim brojem već postoji")
    instrument = Instrument.from_orm(instrument_create)
    session.add(instrument)
    session.commit()
    session.refresh(instrument)
    return instrument

#PUT /instruments/{id} - potpuna zamjena instrumenta
#Pronadi instrument po id-u, ako ne postoji vrati 404, ako postoji zamjeni sve atribute sa novim vrijednostima
@router.put("/{id}", response_model=Instrument)
def update_instrument(id: int, instrument_update: InstrumentCreate, session: Session = Depends(get_session)):
    instrument = session.get(Instrument, id)
    if not instrument:
        raise HTTPException(status_code=404, detail="Instrument nije pronađen")
    instrument_data = instrument_update.dict()
    for key, value in instrument_data.items():
        setattr(instrument, key, value)
    session.add(instrument)
    session.commit()
    session.refresh(instrument)
    return instrument

#PATCH /instruments/{id} - djelimično ažuriranje instrumenta
#Pronadi instrument po id-u, ako ne postoji vrati 404, ako postoji ažuriraj samo one atribute koji su poslani u zahtjevu
@router.patch("/{id}", response_model=Instrument)
def partial_update_instrument(id: int, instrument_update: InstrumentUpdate, session: Session = Depends(get_session)):
    instrument = session.get(Instrument, id)
    if not instrument:
        raise HTTPException(status_code=404, detail="Instrument nije pronađen")
    update_data = instrument_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(instrument, key, value)
    session.add(instrument)
    session.commit()
    session.refresh(instrument)
    return instrument 

#DELETE /instruments/{id} - brisanje instrumenta
@router.delete("/{id}", status_code=204)  
def delete_instrument(id: int, session: Session = Depends(get_session)):
    instrument = session.get(Instrument, id)
    if not instrument:
        raise HTTPException(status_code=404, detail="Instrument nije pronađen")
    session.delete(instrument)
    session.commit()
