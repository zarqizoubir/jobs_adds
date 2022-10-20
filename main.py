from fastapi import Depends, FastAPI, APIRouter
from app import models, schemas
from app.database import engine,SessionLocal
from sqlalchemy.orm import Session

from app.utils.hashing import Hash

app = FastAPI(
    title="Jobs Adds",
)
models.Base.metadata.create_all(bind=engine)

def   get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()



@app.get("/")
def root():
    return {
        "data":[],
        "message":"empty for now",
    }


@app.get("/jobs",response_model=list[schemas.show_jobs],tags=["Jobs"])
def get_all_jobs(db:Session=Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs


@app.get("/jobs/{id}",response_model=schemas.show_jobs,tags=["Jobs"])
def get_all_jobs(id:int,db:Session=Depends(get_db)):
    job = db.query(models.Job).get(id)
    return job





@app.post("/jobs",tags=["Jobs"])
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


@app.get("/users",response_model=list[schemas.show_User],tags=["Users"])
def show_Users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()


    return users    



@app.get("/users/{id}",response_model=schemas.show_User,tags=["Users"])
def show_Users(id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).get(id)


    return user    

@app.post("/users",status_code=202,tags=["Users"])
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