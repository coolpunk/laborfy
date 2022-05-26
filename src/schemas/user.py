import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    username: str
    name: Optional[str] = None
    is_customer: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserWithPwd(User):
    password_hash: str


class UserInDb(BaseModel):
    email: EmailStr
    username: str
    name: Optional[str] = None
    password: str
    is_customer: bool
