from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID, uuid4
import re

from pydantic import BaseModel, validator, root_validator

import main


class Reservation(BaseModel):
    id: Optional[UUID] = uuid4()
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
            raise ValueError("The restaurant opens at 8AM")
        if dateOfReservation > closingDate:
            raise ValueError("The restaurant closes reservations at 8PM")
        if dateOfReservation < datetime.now():
            raise ValueError("Reservations cannot be made in the past")
        return date

    @validator('duration')
    def validator_of_duration(cls, duration):
        if duration < 1:
            raise ValueError("Minimum time of reservation is 1h")
        elif duration > 3:
            raise ValueError("Maximum time of reservation is 3h")
        return duration

    @validator('seatNumber')
    def validator_of_seatNumber(cls, seatNumber):
        if seatNumber < 1:
            raise ValueError("Number of seat must be greater than or equal to 1")
        elif seatNumber > len(main.allTables):
            raise ValueError(f"Number of seat must be less than or equal to {len(main.allTables)}")
        return seatNumber

    @validator('email')
    def validator_of_email(cls, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if not re.search(regex, email):
            raise ValueError("This email number is not valid")
        return email

    @validator('phone')
    def validator_of_phone(cls, phone):
        regex = '(?<!\w)(\(?(\+|00)?48\)?)?[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}(?!\w)'

        if not re.search(regex, phone):
            raise ValueError("This phone number is not valid")
        return phone

    @root_validator(pre=False, skip_on_failure=True)
    def validator_of_values(cls, values):
        if (values['numberOfSeats'] < main.allTables[values['seatNumber'] - 1].min_number_of_seats
                or values['numberOfSeats'] > main.allTables[values['seatNumber'] - 1].max_number_of_seats):
            raise ValueError(
                f"The number of seats at this table must be between {main.allTables[values['seatNumber'] - 1].min_number_of_seats} and "
                f"{main.allTables[values['seatNumber'] - 1].max_number_of_seats}")

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
                    raise ValueError("This table is already reserved during these hours")
        return values


class Table:
    number: int
    min_number_of_seats: int
    max_number_of_seats: int

    def __init__(self, number: int, min_number_of_seats: int, max_number_of_seats: int) -> None:
        self.number = number
        self.min_number_of_seats = min_number_of_seats
        self.max_number_of_seats = max_number_of_seats


class CancellationCode(BaseModel):
    verificationCode: str


class CancellationRequest:
    id: UUID
    verificationCode: str

    def __init__(self, id: UUID, verificationCode: str) -> None:
        self.id = id
        self.verificationCode = verificationCode

    def __eq__(self, other):
        if isinstance(other, CancellationRequest):
            return self.id == other.id and self.verificationCode == other.verificationCode
        return False

    def __hash__(self) -> int:
        return super().__hash__()
