from fastapi import FastAPI

from ..db.database import database
from .users import users_router

app = FastAPI(title="Laborfy")

app.include_router(users_router, prefix="/users", tags=["users"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def startup():
    await database.disconnect()
