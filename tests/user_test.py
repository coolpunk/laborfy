from databases import Database
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from src.handlers import app

SQLALCHEMY_DATABASE_URL = "postgresql://testUser:testPassword@localhost:5432/test"

base = Database(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


client = TestClient(app)


async def test_create_user():
    await base.connect()

    response = client.post(
        "/users/",
        json={
            "email": "user@example.com",
            "username": "string",
            "name": "string",
            "password": "string",
            "is_customer": True
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "user@example.com"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "user@example.com"
    assert data["id"] == user_id

    await base.disconnect()
