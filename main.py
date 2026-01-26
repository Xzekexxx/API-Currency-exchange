from fastapi import FastAPI
from app.routers.auth import router_auth
import uvicorn

app = FastAPI()
app.include_router(router_auth)


if __name__=="__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)