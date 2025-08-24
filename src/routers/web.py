from typing import Annotated

from db.db import get_session
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers.cars import get_cars
from sqlmodel import Session

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.post("/search", response_class=HTMLResponse)
def search(
    size: Annotated[str, Form()],
    doors: Annotated[int, Form()],
    request: Request,
    session: Annotated[Session, Depends(get_session)],
):
    cars = get_cars(size=size, doors=doors, session=session)
    return templates.TemplateResponse(
        "search_results.html", {"request": request, "cars": cars}
    )
