from typing import List

from fastapi import APIRouter, Depends

from .depends import get_user_repository
from ..repository.users import UserRepository
from ..schemas.user import User, UserInDb, UserWithPwd

users_router = APIRouter()

@users_router.get("/", response_model = List[User])
async def read_users(users: UserRepository = Depends(get_user_repository)):
    return await users.get_all()


@users_router.post("/", response_model=User)
async def create(
    user: UserInDb,
    users: UserRepository = Depends(get_user_repository)
    ):
    return await users.add(user) 


@users_router.patch("/", response_model=User)
async def update_user(user_id: int, 
                      user: UserInDb, 
                      users: UserRepository = Depends(get_user_repository)
                      ):
    return await users.update(user_id, user)
