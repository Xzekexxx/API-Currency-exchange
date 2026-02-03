from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.errors.base import CustomExeption
from app.schemas.errors import CustomExeptionModel


async def app_exeption_handler(request: Request, exc: CustomExeption):

    error_response = CustomExeptionModel( status_code=exc.status_code, message=exc.message, er_details=exc.detail)

    return JSONResponse(
        status_code=exc.status_code, content=error_response.model_dump()
    )

async def validator_exceptionhandler(request: Request, exc: RequestValidationError):
     return JSONResponse(
        status_code=422,
        content={
            "error": "Validation error",
            "details": [
                {
                    "field": err["loc"][-1],
                    "message": err["msg"]
                } 
                for err in exc.errors()
            ]
        }
    )