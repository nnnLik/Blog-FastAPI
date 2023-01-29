from datetime import datetime

from sqlalchemy import (
    Column, Table, MetaData,
    Integer, String, DateTime,
    Boolean, JSON,
    ForeignKey, TIMESTAMP, Enum,
)

from .role import role
metadata = MetaData()

user = Table(
    'blog_user',
    metadata,

    Column('id', Integer, primary_key=True, index=True, unique=True),

    Column('username', String, unique=True, nullable=False),
    Column('password', String, nullable=False),

    Column('email', String),
    Column('phone', String),

    Column('date_joined', TIMESTAMP, default=datetime.utcnow()),

    Column('is_admin', Boolean, default=False),
    Column('is_active', Boolean, default=True),

    Column('role_id', Integer, ForeignKey(role.c.id))
)



