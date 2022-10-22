from fastapi import APIRouter,Request,Form,File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

router = APIRouter(
    tags=["Website"]
)

templates = Jinja2Templates("templates")

@router.get("/me",response_class=HTMLResponse)
def me(request:Request):
    return templates.TemplateResponse("index.html",{
        "request":request,
        "title":"Hello World",
        "me":" Ezzoubair Zarqi",
        "data":"None"
    })

@router.post("/me",response_class=HTMLResponse)
async def me(request:Request,file : UploadFile = File(...)):
    new_file= open(f"storage/{file.filename}","wb")
    content =await file.read()
    new_file.write(content)
    return templates.TemplateResponse("index.html",{
        "request":request,
        "title":"Hello World",
        "me":" Ezzoubair Zarqi",
        "data":"None"
    })