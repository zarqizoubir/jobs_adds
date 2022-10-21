from fastapi import APIRouter,Depends,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils import oauth2


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/",response_model=list[schemas.show_jobs])
def get_all_jobs(current_user: schemas.User = Depends(oauth2.get_current_user),db:Session=Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs


@router.get("/{id}",response_model=schemas.show_jobs)
def get_all_jobs(id:int,db:Session=Depends(get_db)):
    job = db.query(models.Job).get(id)
    return job




@router.post("/")
def create_job(request:schemas.Job,db:Session=Depends(get_db)):
    new_job = models.Job(title=request.title,
    description=request.description,
    place=request.place,
    salary=request.salary,
    skills=request.skills,
    user_id=1)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return request



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_job(id :int,db:Session=Depends(get_db)):
    db.query(models.Job).filter("id"==id).delete(synchronize_session=False)

    return {
        "message":"Deleted"
    }