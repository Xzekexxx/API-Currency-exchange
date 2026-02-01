from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Converter(BaseModel):
    amount: int
    from_currency: int
    to_currency: int 