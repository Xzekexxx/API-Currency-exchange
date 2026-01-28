from fastapi import FastAPI
from app.routers.auth import router_auth, router_user
import uvicorn

app = FastAPI()
app.include_router(router_auth)
app.include_router(router_user)


if __name__=="__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)