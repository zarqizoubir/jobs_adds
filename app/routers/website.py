from fastapi import APIRouter,Request,Form,File, UploadFile,Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Website"]
)


templates = Jinja2Templates("templates")

@router.get("/videos",response_class=HTMLResponse)
def me(request:Request,db:Session = Depends(get_db)):
    videos : list[models.Video] = db.query(models.Video).all()

    return templates.TemplateResponse("videos.html",{
        "request":request,
        "length":videos.__len__(),
        "videos":videos
    })

@router.get("/videos/{id}",response_class=HTMLResponse)
def anime_by_id(id:int,request:Request,db:Session = Depends(get_db)):
    video :models.Video = db.query(models.Video).get(id)
    print(video.path)
    return templates.TemplateResponse("video.html",{
        "request":request,
        "name":video.filename,
        "path":video.path,
        "id":id
    })

@router.get("/upload")
async def upload(request:Request):
    return templates.TemplateResponse("upload.html",{
        "request":request,  
    })



@router.post("/upload")
async def upload(request:Request,file:UploadFile =File(...),db:Session = Depends(get_db)):
    path = f"storage/{file.filename}"
    new_file = open(path,"wb")
    content =await file.read()
    new_file.write(content)
    new_file_model = models.Video(
        filename=file.filename,
        path=path
    )
    db.add(new_file_model)
    db.commit()
    db.refresh(new_file_model)
    return templates.TemplateResponse("upload.html",{
        "request":request,
    })