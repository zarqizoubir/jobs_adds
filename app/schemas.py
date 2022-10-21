from pydantic import BaseModel
from typing import List



class Job(BaseModel):
    title:str = "Job title"
    description:str ="Job Description"
    place:str = "Headquarter ,Working place"
    salary:float = 0.0
    skills:str = "skills"

    

class JobBase(Job):
    class Config:
        orm_mode = True

class User(BaseModel):
    username:str = "username"
    email:str ="email"
    password:str = "password"

class show_User(BaseModel):
    username:str
    email:str
    jobs:List[JobBase]

    class Config:
        orm_mode = True


class show_jobs(BaseModel):
    title:str
    description:str
    place:str
    salary:float
    skills:str
    poster: show_User

    class Config:
        orm_mode = True
