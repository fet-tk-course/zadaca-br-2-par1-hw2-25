from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session
from models_b import Measurement

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
