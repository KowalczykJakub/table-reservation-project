from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Reservation(BaseModel):
    id: Optional[UUID] = uuid4()
    date: datetime
    duration: int
    seatNumber: int
    numberOfSeats: int
    fullName: str
    phone: str
    email: str
