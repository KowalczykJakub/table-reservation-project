from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException

from models import Reservation

app = FastAPI()

reservations: List[Reservation] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/reservations")
async def getReservations():
    return reservations


@app.post("/reservations")
async def addReservation(reservation: Reservation):
    reservations.append(reservation)
    return {"id": reservation.id}


@app.delete("/reservations/{id}")
async def deleteReservation(id: UUID):
    for reservation in reservations:
        if reservation.id == id:
            reservations.remove(reservation)
            return 
        raise HTTPException(status_code=404, detail=f"Reservation with id: {id} does not exist")

