from fastapi import FastAPI
from app.auth.routes import auth_router
from app.datanyze.routers import datanyze_router
from contextlib import asynccontextmanager
from app.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Sever is starting ...")
    await init_db()
    yield
    print("Sever has been stopped")

version = "v1"

description = """
    Some description ...
"""

version_prefix = f"/api/{version}"

app = FastAPI(
    title="Datanyze",
    description=description,
    version=version,
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
    lifespan=life_span,
)

app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(datanyze_router, prefix=f"{version_prefix}/datanyze", tags=["datanyze"])
