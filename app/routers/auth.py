from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.database.database import get_session
from app.schemas.users import User
from app.models.models import Users
from app.security.security import hash_password, validate_password, create_jwt_token, get_current_user
from app.errors.auth import UserNotFoundExeption, UserAlreadyExistsException, InvalidCredentialsException

router_auth = APIRouter(tags=["auth"])
router_user = APIRouter(prefix="/user", tags=["User"])

@router_auth.post("/reg")
async def register_user(user_data: User, db: AsyncSession = Depends(get_session)):
    get_user_from_db = await db.execute(select(Users).where(Users.username==user_data.username))
    user = get_user_from_db.scalar_one_or_none()
    if user:
        raise UserAlreadyExistsException(detail="user already exists")
    
    hashed_password = hash_password(user_data.password)

    create_new_user = Users(
        username = user_data.username,
        email = user_data.email,
        password = hashed_password.decode('utf-8')
    )

    db.add(create_new_user)
    await db.commit()
    await db.refresh(create_new_user)

    return {'message': 'You have registered successfully'}

@router_auth.post("/login")
async def login_user(user_in : OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    try:
        check_user = (await db.execute(select(Users).where(Users.username==user_in.username))).scalar_one_or_none()
        user_password = validate_password(user_in.password, check_user.password)

        if check_user and user_password:
            token = create_jwt_token({"sub": user_in.username})

            return {"access_token": token, 
                    "token_type": "bearer"}
        else:
            raise UserNotFoundExeption(detail="User was not found")

    except:
        raise InvalidCredentialsException(detail="Incorrect data")

@router_user.get("/about_user")
async def about_user(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username,
            "email": current_user.email}