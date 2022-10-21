from datetime import timedelta
from fastapi import APIRouter, Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils.hashing import Hash


router = APIRouter(
    tags=["authentification "]
)


@router.post("/login")
def login(request:OAuth2PasswordRequestForm= Depends(),db:Session=Depends(get_db)):
    user : models.User = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=404,detail="Invalid Credentials")


    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail="Password Not Correct")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
