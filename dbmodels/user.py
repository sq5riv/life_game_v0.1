from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable= False)
    mail = Column(String, nullable= False)
    passwd = Column(String, nullable= False)
    logedin = Column(String, nullable= False)
    blocked = Column(Boolean)
