from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    mail = Column(String)
    passwd = Column(String)
    logedin = Column(String)
    blocked = Column(String)
