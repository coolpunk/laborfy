from starlette.config import Config

config = Config(".env_dist")

DATABASE_URL = config("DB_URL", cast=str)
