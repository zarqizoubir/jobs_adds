from pydantic import BaseModel

class Job(BaseModel):
    title:str
    description:str
    place:str
    salary:float
    skills:str


class User(BaseModel):
    username:str
    email:str
    password:str

class show_User(BaseModel):
    username:str
    email:str

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
