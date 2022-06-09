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


class Table:
    number: int
    min_number_of_seats: int
    max_number_of_seats: int

    def __init__(self, number: int, min_number_of_seats: int, max_number_of_seats: int) -> None:
        self.number = number
        self.min_number_of_seats = min_number_of_seats
        self.max_number_of_seats = max_number_of_seats

# class Table(BaseModel):
#     number: int
#     minNumberOfSeats: int
#     maxNumberOfSeats: int


