from datetime import datetime, timedelta
from typing import List, Set
from uuid import UUID
import random
import math

from fastapi import FastAPI, HTTPException

import initialize_data
import mail_sender
from models import Reservation, Table, CancellationRequest, CancellationCode

app = FastAPI()

reservations: List[Reservation] = []
allTables: List[Table] = initialize_data.readTablesFromJsonFile()
cancellationRequests: Set[CancellationRequest] = set()


@app.get("/emailTest")
async def root():
    return mail_sender.sendEmail('siema.siema@gmail.com', 'Siema', 'Siema, ale to content')


@app.get("/reservations")
async def getReservations():
    return reservations


@app.get("/tables")
async def getTables():
    return allTables


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
            cancellationRequests.add(CancellationRequest(id, code))
            return "Verification code has been sent!"
    raise HTTPException(status_code=404, detail=f"Reservation with id: {id} does not exist")


@app.delete("/reservations/{id}")
async def deleteReservation(id: UUID, code: CancellationCode):
    for request in cancellationRequests:
        if request.id == id:
            if request.verificationCode == code.verificationCode:
                for reservation in reservations:
                    if reservation.id == id:
                        reservations.remove(reservation)
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

