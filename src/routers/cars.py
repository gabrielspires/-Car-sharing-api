import uuid
from typing import Annotated

from db.db import get_session
from fast_api.schemas import Car, CarInput, CarOutput, Trip, TripInput
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

router = APIRouter(prefix="/api/cars")


@router.get("/")
def get_cars(
    session: Annotated[Session, Depends(get_session)],
    size: str | None = None,
    doors: int | None = None,
) -> list:
    query = select(Car)
    if size:
        query = query.where(Car.size == size)
    if doors:
        query = query.where(Car.doors == doors)
    return list(session.exec(query).all())


@router.get("/{id}")
def car_by_id(session: Annotated[Session, Depends(get_session)], id) -> CarOutput:
    id = uuid.UUID(id)
    car = session.get(Car, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.post("/")
def add_car(session: Annotated[Session, Depends(get_session)], car: CarInput) -> Car:
    new_car = Car.model_validate(car)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car


@router.delete("/{id}", status_code=204)
def remove_car(session: Annotated[Session, Depends(get_session)], id: str) -> None:
    id = uuid.UUID(id)
    car = session.get(Car, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.put("/{id}")
def change_car(
    session: Annotated[Session, Depends(get_session)], id: str, new_data: CarInput
) -> Car:
    id = uuid.UUID(id)
    car = session.get(Car, id)
    if car:
        car.fuel = new_data.fuel
        car.transmission = new_data.transmission
        car.size = new_data.size
        car.doors = new_data.doors
        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.post("/{car_id}/trips")
def add_trip(
    session: Annotated[Session, Depends(get_session)],
    car_id: str,
    trip_input: TripInput,
) -> Trip:
    car_id = uuid.UUID(car_id)
    car = session.get(Car, car_id)
    if car:
        new_trip = Trip.model_validate(trip_input, update={"car_id": car_id})
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
