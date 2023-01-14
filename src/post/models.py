from core.database import Base

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    """Post table model"""

    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True, index=True, unique=True)

    title = Column(String)
    content = Column(String(350))

    date = Column(DateTime)

    # tags = ...
    user = Column(Integer, ForeignKey('blog_user.id'))

    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)

    user_id = relationship('User')