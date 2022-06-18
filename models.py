import uuid
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID
import re

from fastapi import HTTPException
from pydantic import BaseModel, validator, root_validator, Field

import main


class Reservation(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid.uuid4)
    date: str
    duration: int
    seatNumber: int
    numberOfSeats: int
    fullName: str
    phone: str
    email: str

    @validator('date')
    def validator_of_date(cls, date):
        dateOfReservation = datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
        openingDate = dateOfReservation.replace(hour=8, minute=0, second=0)
        closingDate = dateOfReservation.replace(hour=20, minute=0, second=0)

        if dateOfReservation < openingDate:
            raise HTTPException(status_code=400, detail="The restaurant opens at 8AM")
        if dateOfReservation > closingDate:
            raise HTTPException(status_code=400, detail="The restaurant closes reservations at 8PM")
        if dateOfReservation < datetime.now():
            raise HTTPException(status_code=400, detail="Reservations cannot be made in the past")
        return date

    @validator('duration')
    def validator_of_duration(cls, duration):
        if duration < 1:
            raise HTTPException(status_code=400, detail="Minimum time of reservation is 1h")
        elif duration > 3:
            raise HTTPException(status_code=400, detail="Maximum time of reservation is 3h")
        return duration

    @validator('seatNumber')
    def validator_of_seatNumber(cls, seatNumber):
        if seatNumber < 1:
            raise HTTPException(status_code=400, detail="Number of seat must be greater than or equal to 1")
        elif seatNumber > len(main.allTables):
            raise HTTPException(status_code=400, detail=f"Number of seat must be less than or equal to {len(main.allTables)}")
        return seatNumber

    @validator('email')
    def validator_of_email(cls, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if not re.search(regex, email):
            raise HTTPException(status_code=400, detail="This email number is not valid")
        return email

    @validator('phone')
    def validator_of_phone(cls, phone):
        regex = '(?<!\w)(\(?(\+|00)?48\)?)?[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}(?!\w)'

        if not re.search(regex, phone):
            raise HTTPException(status_code=400, detail="This phone number is not valid")
        return phone

    @root_validator(pre=False, skip_on_failure=True)
    def validator_of_values(cls, values):
        if (values['numberOfSeats'] < main.allTables[values['seatNumber'] - 1].minNumberOfSeats
                or values['numberOfSeats'] > main.allTables[values['seatNumber'] - 1].maxNumberOfSeats):
            raise HTTPException(status_code=400, detail=
                f"The number of seats at this table must be between {main.allTables[values['seatNumber'] - 1].minNumberOfSeats} and "
                f"{main.allTables[values['seatNumber'] - 1].maxNumberOfSeats}")

        dateOfStart = datetime.strptime(values['date'], '%Y/%m/%d %H:%M:%S')
        dateOfFinish = dateOfStart + timedelta(hours=values['duration'])
        reservations = main.reservations
        for reservation in reservations:
            start = datetime.strptime(reservation.date, '%Y/%m/%d %H:%M:%S')
            finish = start + timedelta(hours=reservation.duration)
            if reservation.seatNumber == values['seatNumber']:
                if (dateOfFinish <= start) or (dateOfStart >= finish):
                    pass
                else:
                    raise HTTPException(status_code=403, detail="This table is already reserved during these hours")

        return values


class Table:
    number: int
    minNumberOfSeats: int
    maxNumberOfSeats: int

    def __init__(self, number: int, minNumberOfSeats: int, maxNumberOfSeats: int) -> None:
        self.number = number
        self.minNumberOfSeats = minNumberOfSeats
        self.maxNumberOfSeats = maxNumberOfSeats


class Dish:
    name: str
    description: str
    price: float
    type: str

    def __init__(self, name: str, description: str, price: float, type: str) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.type = type


class CancellationCode(BaseModel):
    verificationCode: str


class CancellationRequest:
    id: UUID
    verificationCode: str

    def __init__(self, id: UUID, verificationCode: str) -> None:
        self.id = id
        self.verificationCode = verificationCode


class TableFilterModel(BaseModel):
    date: str
    duration: int
    numberOfSeats: int

    @validator('date')
    def validator_of_date(cls, date):
        dateOfReservation = datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
        openingDate = dateOfReservation.replace(hour=8, minute=0, second=0)
        closingDate = dateOfReservation.replace(hour=20, minute=0, second=0)

        if dateOfReservation < openingDate:
            raise HTTPException(status_code=400, detail="The restaurant opens at 8AM")
        if dateOfReservation > closingDate:
            raise HTTPException(status_code=400, detail="The restaurant closes reservations at 8PM")
        if dateOfReservation < datetime.now():
            raise HTTPException(status_code=400, detail="Reservations cannot be made in the past")
        return date

    @validator('duration')
    def validator_of_duration(cls, duration):
        if duration < 1:
            raise HTTPException(status_code=400, detail="Minimum time of reservation is 1h")
        elif duration > 3:
            raise HTTPException(status_code=400, detail="Maximum time of reservation is 3h")
        return duration