import uuid

from sqlmodel import Field, Relationship, SQLModel


class TripInput(SQLModel):
    start: int
    end: int
    description: str


class TripOutput(TripInput):
    id: uuid.UUID


class Trip(TripInput, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    car_id: uuid.UUID = Field(foreign_key="car.id")
    car: "Car" = Relationship(back_populates="trips")


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"size": "m", "doors": 5, "transmission": "manual", "fuel": "hybrid"}
            ]
        }
    }


class Car(CarInput, table=True):
    id: uuid.UUID | None = Field(primary_key=True, default_factory=uuid.uuid4)
    trips: list[Trip] = Relationship(back_populates="car")


class CarOutput(CarInput):
    id: uuid.UUID
    trips: list[TripOutput] = []
