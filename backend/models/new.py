from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.database import Base

# categoria da notícia
# título da notícia
# hora publicada
# texto da notícia

class New(Base):
    __tablename__ = "news"

    id = Column(Integer,primary_key=True,index=True,unique=True)
    title = Column(String,index=True)
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    category = Column(String,index=True)