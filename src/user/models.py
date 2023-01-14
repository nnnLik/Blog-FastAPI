from core.database import Base

from sqlalchemy import Column, String, Integer, DateTime, Boolean


class User(Base):
    """User table model"""

    __tablename__ = 'blog_user'

    id = Column(Integer, primary_key=True, index=True, unique=True)

    username = Column(String, unique=True)
    password = Column(String)

    email = Column(String, unique=True)
    phone = Column(String, unique=True)

    date_joined = Column(DateTime)

    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
