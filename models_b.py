from sqlmodel import SQLModel, Field
from typing import Optional

class Measurement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    measurement_type: str = Field(index=True)
    duration_minutes: int
    is_automated: bool = False
    required_accuracy: float
    description: Optional[str] = None



class MeasurementCreate(SQLModel):
    measurement_type: str
    duration_minutes: int
    is_automated: bool = False
    required_accuracy: float
    description: Optional[str] = None
 

class MeasurementUpdate(SQLModel):
    measurement_type: Optional[str] = None
    duration_minutes: Optional[int] = None
    is_automated: Optional[bool] = None
    required_accuracy: Optional[float] = None
    description: Optional[str] = None
 