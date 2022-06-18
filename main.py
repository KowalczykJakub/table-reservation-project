from datetime import datetime, timedelta
from typing import List
from uuid import UUID
import random
import math

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

import initialize_data
import mail_sender
from models import Reservation, Table, CancellationRequest, Dish, TableFilterModel

app = FastAPI()

origins = ["http://localhost:4200",
           "localhost:4200",
           "https://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

reservations: List[Reservation] = []
allTables: List[Table] = initialize_data.readTablesFromJsonFile()
filteredTables: List[Table] = []
allDishes: List[Dish] = initialize_data.readDishesFromJsonFile()
cancellationRequests: List[CancellationRequest] = []


@app.get("/reservations")
async def getReservations():
    return reservations


@app.get("/dishes")
async def getReservations():
    return allDishes


@app.get("/tables")
async def getTables():
    return filteredTables


@app.post("/tables")
async def filterTables(tableFilterModel: TableFilterModel):
    filteredList = []
    for table in allTables:
        if (table.minNumberOfSeats <= tableFilterModel.numberOfSeats
            and table.maxNumberOfSeats >= tableFilterModel.numberOfSeats):
            filteredList.append(table)
    dateOfStart = datetime.strptime(tableFilterModel.date, '%Y/%m/%d %H:%M:%S')
    dateOfFinish = dateOfStart + timedelta(hours=tableFilterModel.duration)

    for reservation in reservations:

        start = datetime.strptime(reservation.date, '%Y/%m/%d %H:%M:%S')
        finish = start + timedelta(hours=reservation.duration)

        if not ((dateOfFinish <= start) or (dateOfStart >= finish)):
            for table in filteredList:
                if table.number == reservation.seatNumber:
                    filteredList.remove(table)
    global filteredTables
    filteredTables = filteredList

    return filteredList


@app.post("/reservations")
async def addReservation(reservation: Reservation):
    reservations.append(reservation)
    mail_sender.sendEmail(reservation.email, f"Reservation for {reservation.date}\n",
                              f"Id: {reservation.id}\n"
                              f"Date: {reservation.date}\n"
                              f"Duration: {reservation.duration}\n"
                              f"Table number: {reservation.seatNumber}\n"
                              f"Number of seats: {reservation.numberOfSeats}\n"
                              f"Full name: {reservation.fullName}\n"
                              f"Phone number: {reservation.phone}\n"
                              f"Email: {reservation.email}\n")
    return {"id": reservation.id}


@app.put("/reservations/{id}")
async def cancellationOfReservationRequest(id: UUID):
    for reservation in reservations:
        if reservation.id == id:
            date = datetime.strptime(reservation.date, '%Y/%m/%d %H:%M:%S')
            if date <= datetime.now() + timedelta(hours=2):
                raise HTTPException(status_code=403, detail="It's too late to cancel your reservation")
            code = generateCode()
            mail_sender.sendVerificationCode(reservation.email, code)
            # Tutaj pętla z usunięciem wszystkich requestów z tym samym id
            for request in cancellationRequests:
                if request.id == id:
                    cancellationRequests.remove(request)
            cancellationRequests.append(CancellationRequest(id, code))
            return "Verification code has been sent!"
    raise HTTPException(status_code=404, detail=f"Reservation with id: {id} does not exist")


@app.delete("/reservations/{id}/{code}")
async def deleteReservation(id: UUID, code: str):
    for request in cancellationRequests:
        if request.id == id:
            if request.verificationCode == code:
                for reservation in reservations:
                    if reservation.id == id:
                        reservations.remove(reservation)
                        mail_sender.sendEmail(reservation.email, "Your reservation has been cancelled",
                                              f"Reservation with id {reservation.id} has been cancelled")
                cancellationRequests.remove(request)
            else:
                raise HTTPException(status_code=400, detail="Verification code is not correct!")
            return "Your reservation has been cancelled!"
    raise HTTPException(status_code=404, detail="You have to send cancellation request firstly!")


def generateCode():
    random_code = ""
    for i in range(6):
        digit = math.floor(random.random() * 10)
        random_code += str(digit)
    return random_code

