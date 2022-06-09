from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException

import initialize_data
import mail_sender
from models import Reservation, Table

app = FastAPI()

reservations: List[Reservation] = []
allTables: List[Table] = initialize_data.readTablesFromJsonFile()


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
    return {"id": reservation.id}


@app.delete("/reservations/{id}")
async def deleteReservation(id: UUID, code: str):
    for reservation in reservations:
        if reservation.id == id:
            reservations.remove(reservation)
            return
        raise HTTPException(status_code=404, detail=f"Reservation with id: {id} does not exist")

