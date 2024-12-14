from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

auth_router = APIRouter()

@auth_router.get("/", deprecated=True)
async def say_hello():
    return {"message": "Hello From Auth"}

@auth_router.get("/man")
async def say_man():
    return {"message": "Hello Man From Auth"}