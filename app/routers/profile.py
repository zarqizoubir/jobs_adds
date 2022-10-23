from fastapi import APIRouter, Request, Form, File, UploadFile, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Profile"],
    prefix="/me"
)


templates = Jinja2Templates("templates")


@router.get("/")
def my_Profile(request: Request):
    return templates.TemplateResponse("profile/me.html", {
        "request": request,
    })


@router.get("/update", response_class=HTMLResponse)
def update_profile(request: Request):
    return templates.TemplateResponse("profile/update.html", {
        "request": request,
    })
