from datetime import datetime, timedelta

from jose import JWTError,jwt

from app.schemas import TokenData


SECRET_KEY = "93495dd7b3af5aab37372f499e264a641fa86c8d01f1ef4be1e15be70e96088099f3f6c3d1bdab487cb6e255e5d1039b4f4f3d3266cf03eaf300a28eb2409d6a1f4bc62fdf022aef21f856a9194fb15bac3bf35eda042201d3558e0dc2c9b8c8a47df1921134ab9c04c07afc3f2a50c1d578033a9458c29fa614918885c61a91)çuqpvuipsdviupdsiudgvusdgvèçàvgvà_ègg°°°+++°0099900HUDHUHDUBBUCGUVGVUIDHVOPGVIOPVYPVYPG9VBIOYVYIPVVPIDO"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=100



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except JWTError:
        raise credentials_exception
    