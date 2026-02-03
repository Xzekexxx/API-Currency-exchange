from fastapi import FastAPI
from app.handlers.exceptions import app_exeption_handler, validator_exceptionhandler
from app.errors.base import CustomExeption
from fastapi.exceptions import RequestValidationError
from app.routers.auth import router_auth, router_user
from app.routers.currency import router_currency
import uvicorn

app = FastAPI()
app.include_router(router_auth)
app.include_router(router_user)
app.include_router(router_currency)

app.add_exception_handler(CustomExeption, app_exeption_handler)
app.add_exception_handler(RequestValidationError, validator_exceptionhandler)


if __name__=="__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)