from datetime import datetime

from sqlalchemy import (
    Column, Table, MetaData,
    Integer, String, ForeignKey, TIMESTAMP,
)

from src.user.models.profile import profile
from src.post.models.tag import tag

metadata = MetaData()

post = Table(
    'blog_post',
    metadata,

    Column('id', Integer, primary_key=True, index=True, unique=True),

    Column('title', String, nullable=False),
    Column('content', String),

    Column('created_date', TIMESTAMP, default=datetime.utcnow()),

    Column('view_count', Integer, default=0),
    Column('like_count', Integer, default=0),

    Column('user_id', Integer, ForeignKey(profile.c.id)),
    Column('tags', ForeignKey(tag.c.id), nullable=False),
)
