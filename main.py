from fastapi import Depends, FastAPI, Request
from app import models
from app.database import engine
from app.routers import jobs, users, auth, storage, website, profile
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Jobs Adds",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/storage", StaticFiles(directory="storage"), name="storage")
app.mount("/videos/storage", StaticFiles(directory="storage"), name="storage")


models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(auth.router)
app.include_router(storage.router)
app.include_router(website.router)
app.include_router(profile.router)


@app.get("/")
def root():
    return {
        "data": [],
        "message": "empty for now",
    }
