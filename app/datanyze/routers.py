from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

datanyze_router = APIRouter()

@datanyze_router.get("/")
async def say_hello():
    return {"message": "Hello From Books!"}
