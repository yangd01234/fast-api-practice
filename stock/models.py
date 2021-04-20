from .database import Base
from sqlalchemy import Column, Integer, String

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    description = Column(String)