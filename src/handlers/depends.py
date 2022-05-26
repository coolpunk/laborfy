from ..db.database import database
from ..repository.users import UserRepository


def get_user_repository() -> UserRepository:
    return UserRepository(database)
