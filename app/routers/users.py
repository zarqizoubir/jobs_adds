from fastapi import APIRouter,Depends
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..CRUD import user_crud


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get("/",response_model=list[schemas.show_User])
def show_Users(db:Session=Depends(get_db)):
    return user_crud.query_all_users(db=db)



@router.get("/{id}",response_model=schemas.show_User)
def show_Users(id:int,db:Session=Depends(get_db)): 
    return user_crud.query_user_by_id(db=db,id=id)


@router.post("/",status_code=202)
def show_Users(request:schemas.User,db:Session=Depends(get_db)):
    return user_crud.create_user(request=request,db=db)