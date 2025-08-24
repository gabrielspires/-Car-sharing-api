from contextlib import asynccontextmanager

import uvicorn
from db.db import engine
from fastapi import FastAPI
from routers import cars, web
from sqlmodel import SQLModel


# Runs AFTER all code is loaded
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before execution
    SQLModel.metadata.create_all(engine)
    yield  # Pauses lifespan() and gives control to the API
    # After execution
    pass


app = FastAPI(title="Car Sharing", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)
