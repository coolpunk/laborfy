import datetime
from typing import List, Optional

from .base import BaseRepository
from ..db.models import users
from ..schemas.user import UserInDb, UserWithPwd, User
from ..utlis.security import hash_password


class UserRepository(BaseRepository):
    async def add(self, user: UserInDb) -> User:
        user = UserWithPwd(
            email=user.email,
            username=user.username,
            name=user.name,
            password_hash=hash_password(user.password),
            is_customer=user.is_customer,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user


    async def update(self, user_id: int, user: UserInDb) -> User:
        user = UserWithPwd(
            email=user.email,
            username=user.username,
            name=user.name,
            password_hash=hash_password(user.password),
            is_customer=user.is_customer,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = users.update().where(users.c.id == user_id).values(**values)
        await self.database.execute(query)
        return user

    
    async def get_all(self) -> List[User]:
        query = users.select()
        obj = await self.database.fetch_all(query)
        return [User.parse_obj(d) for d in obj]


    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = users.select().where(users.c.id == user_id).first()
        obj = await self.database.fetch_one(query)
        if not obj:
            return None
        return User.parse_obj(obj)


    async def get_by_username(self, username: str) -> User:
        query = users.select().where(users.c.username == username).first()
        obj = await self.database.fetch_one(query)
        if not obj:
            return None
        return User.parse_obj(obj)

    
    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email).first()
        obj = await self.database.fetch_one(query)
        if not obj:
            return None
        return User.parse_obj(obj)


    async def delete(user_id: int):
        pass
