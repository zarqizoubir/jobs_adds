from fastapi import APIRouter,Depends
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter()


@router.get("/jobs",response_model=list[schemas.show_jobs],tags=["Jobs"])
def get_all_jobs(db:Session=Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs


@router.get("/jobs/{id}",response_model=schemas.show_jobs,tags=["Jobs"])
def get_all_jobs(id:int,db:Session=Depends(get_db)):
    job = db.query(models.Job).get(id)
    return job





@router.post("/jobs",tags=["Jobs"])
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
