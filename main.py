from fastapi import FastAPI
import uvicorn

from db.base import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def startup():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello world!"}


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
