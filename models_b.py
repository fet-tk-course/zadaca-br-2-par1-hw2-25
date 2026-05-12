from sqlmodel import SQLModel, Field
from typing import Optional

class Measurement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    measurement_type: str = Field(index=True)
    duration_minutes: int
    is_automated: bool = False
    required_accuracy: float
    description: Optional[str] = None

