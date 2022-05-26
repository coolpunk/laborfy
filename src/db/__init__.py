from .database import metadata, engine
from .models import users, offers

metadata.create_all(bind=engine)
