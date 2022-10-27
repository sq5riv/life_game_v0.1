from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Rules(Base):
    __tablename__ = 'Rules'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(Integer)
    rules = Column(JSON)