from .. import database,models,schemas
from ..utils.hashing import Hash


def query_all_users(db):
    users = db.query(models.User).all()
    return users


def query_user_by_id(id:int,db):
    user = db.query(models.User).get(id)
    return user 


def create_user(request:schemas.User,db):
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