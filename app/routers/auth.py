from fastapi import APIRouter


router_auth = APIRouter(prefix="/auth")

@router_auth.post("/reg")
async def register_user():
    return

@router_auth.post("/login")
async def login_user():
    return