from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    username: str = Field(min_length=5, max_length=12)
    email: EmailStr
    password: str

    class Config:
        from_attributes = True