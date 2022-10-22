from sqlalchemy import ForeignKey, Integer, String, Column, Float
from sqlalchemy.orm import relationship
from .database import Base


class Job(Base):
    __tablename__="jobs"
    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    place=Column(String)
    salary=Column(Float)
    skills=Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))

    poster = relationship("User",back_populates="jobs")

class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password= Column(String)

    jobs= relationship("Job",back_populates="poster")



class Video(Base):
    __tablename__="videos"
    id = Column(Integer,primary_key=True,index=True)
    filename = Column(String)
    path = Column(String)