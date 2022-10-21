from fastapi import Depends, FastAPI,Request
from app import models
from app.database import engine
from app.routers import jobs,users,auth

app = FastAPI(
    title="Jobs Adds",
)
models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {
        "data":[],
        "message":"empty for now",
    }

