from core.database import Base

from sqlalchemy import (
    Column, String, Integer,
    DateTime, Boolean, Text,
    ForeignKey, Enum)


class UserGenders(Enum):
    """User Genders choice type class"""

    male = 'male'
    female = 'female'
    other = 'other'

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


class Profile(Base):
    """User table model"""

    __tablename__ = 'blog_profile'

    id = Column(Integer, primary_key=True, index=True, unique=True)

    first_name = Column(String)
    second_name = Column(String)

    sex = Column(Enum(UserGenders))

    birthdate = Column(DateTime)
    biography = Column(Text)

    github = Column(String)
    linkedin = Column(String)
    twitter = Column(String)
    facebook = Column(String)

    favourite = Column(Integer, ForeignKey('blog_post.id'))



