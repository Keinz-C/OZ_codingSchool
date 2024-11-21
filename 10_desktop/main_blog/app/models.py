from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database import Base


class BlogPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)
    created_at = Column(DateTime)
