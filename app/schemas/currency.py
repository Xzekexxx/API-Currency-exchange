from pydantic import BaseModel

class Converter(BaseModel):
    from_currency: str
    to_currency: str 
    amount: int