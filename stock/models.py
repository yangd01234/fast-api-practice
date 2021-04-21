from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # relationship that back_populates to reference
    owner = relationship("User", back_populates="stocks")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    stocks = relationship('Stock', back_populates="owner")