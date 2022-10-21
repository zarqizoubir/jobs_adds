from fastapi import APIRouter,Depends
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils.hashing import Hash



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get("/",response_model=list[schemas.show_User])
def show_Users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users



@router.get("/{id}",response_model=schemas.show_User)
def show_Users(id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).get(id)
    return user  

@router.post("/",status_code=202)
def show_Users(request:schemas.User,db:Session=Depends(get_db)):
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password) 
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message":"created"
    }