import datetime

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean, DateTime
from .database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String, unique=True),
    Column("username", String, unique=True, nullable=False),
    Column("name", String),
    Column("password_hash", String, nullable=False),
    Column("is_customer", Boolean),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)

offers = Table(
    "offers",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey(users.columns.id, ondelete='CASCADE'), nullable=False),
    Column("title", String, nullable=False),
    Column("description", String),
    Column("sallary_from", Integer),
    Column("sallary_to", Integer),
    Column("is_active", Boolean),
    Column("created_at", DateTime, default=datetime.datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.datetime.utcnow)
)
