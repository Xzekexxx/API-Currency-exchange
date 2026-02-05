import jwt
import datetime 
import bcrypt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Dict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import User
from app.database.database import get_session
from app.models.models import Users
from app.core.config import settings
from app.errors.auth import UserNotFoundExeption

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_jwt_token(data: Dict):
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        return {"error": "token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "invalid token"}

async def get_current_user(username: str = Depends(get_user_from_token), db: AsyncSession = Depends(get_session)):
    current_user = (await db.execute(select(Users).where(username == Users.username))).scalar_one_or_none()
    if current_user:
        return User.model_validate(current_user)

    raise UserNotFoundExeption(detail="User not found")

def hash_password(password: str):
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)

def validate_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())