'''
https://docs.sqlalchemy.org/en/13/orm/tutorial.html
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define database url
SQLACHEMY_DATABASE_URL = 'sqlite:///./stock.db'

# create engine
engine = create_engine(SQLACHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# create session maker
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

# define base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        # THIS IS VERY IMPORTANT.  Yield is a generator.  Make sure to close()
        yield db
    finally:
        db.close()