from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Deck(Base):
    __tablename__ = 'Deck'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable= False)
    version = Column(Integer, nullable= False)