from fastapi import  Depends
from .. import models


def query_all_jobs(current_user,db):
    jobs = db.query(models.Job).all()
    return jobs


def query_job_by_id(id:int,db):
    job = db.query(models.Job).get(id)
    return job



def create_job(request,db):
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


def delete_job(db,id:int):
    db.query(models.Job).filter("id"==id).delete(synchronize_session=False)

    return {
        "message":"Deleted"
    }