from pydantic import BaseModel

class CustomExeptionModel(BaseModel):
    er_details: str
    status_code: int
    message: str