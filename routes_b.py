from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session
from models_b import Measurement, MeasurementCreate, MeasurementUpdate

router = APIRouter(prefix="/measurements", tags=["Mensurations"])

@router.get("/", response_model=list[Measurement])
def get_measurements(session: Session = Depends(get_session)):
    query = select(Measurement)
    measurements = session.exec(query).all()
    return measurements


@router.get("/{id}", response_model=Measurement)
def get_measurement(id: int, session: Session = Depends(get_session)):
    measurement = session.get(Measurement, id)
    if not measurement:
        raise HTTPException(status_code=404, detail="Mjerenje nije pronađeno")
    return measurement



@router.post("/", response_model=Measurement, status_code=201)
def create_measurement(measurement_create: MeasurementCreate, session: Session = Depends(get_session)):
    db_measurement = Measurement.model_validate(measurement_create)   
    session.add(db_measurement)
    session.commit()
    session.refresh(db_measurement)
    return db_measurement


@router.put("/{id}", response_model=Measurement)
def update_measurement(id: int, measurement_update: MeasurementCreate, session: Session = Depends(get_session)):
    db_measurement = session.get(Measurement, id)
    if not db_measurement:
        raise HTTPException(status_code=404, detail="Mjerenje nije pronađeno")
    measurement_data = measurement_update.model_dump()
    for key, value in measurement_data.items():
        setattr(db_measurement, key, value)
    session.add(db_measurement)
    session.commit()
    session.refresh(db_measurement)
    return db_measurement


@router.patch("/{id}", response_model=Measurement)
def partial_update_measurement(id: int, measurement_patch: MeasurementUpdate, session: Session = Depends(get_session)):
    db_measurement = session.get(Measurement, id)
    if not db_measurement:
        raise HTTPException(status_code=404, detail="Mjerenje nije pronađeno")
    update_data = measurement_patch.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_measurement, key, value)
    session.add(db_measurement)
    session.commit()
    session.refresh(db_measurement)
    return db_measurement


@router.delete("/{id}", status_code=204)
def delete_measurement(id: int, session: Session = Depends(get_session)):
    db_measurement = session.get(Measurement, id)
    if not db_measurement:
        raise HTTPException(status_code=404, detail="Mjerenje nije pronađeno")
    session.delete(db_measurement)
    session.commit()
    return None