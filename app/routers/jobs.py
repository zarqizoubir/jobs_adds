from fastapi import APIRouter,Depends,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils import oauth2
from ..CRUD import job_crud

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/",response_model=list[schemas.show_jobs])
def get_all_jobs(current_user: schemas.User = Depends(oauth2.get_current_user),db:Session=Depends(get_db)):
    return job_crud.query_all_jobs(current_user=current_user,db=db)



@router.get("/{id}",response_model=schemas.show_jobs)
def get_jobs(id:int,db:Session=Depends(get_db)):
    return job_crud.query_job_by_id(db=db,id=id)




@router.post("/")
def create_job(request:schemas.Job,db:Session=Depends(get_db)):
    return job_crud.create_job(db=db,request=request)



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_job(id :int,db:Session=Depends(get_db)):
    return job_crud.delete_job(db=db,id=id)