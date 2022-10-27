from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class Games(Base):
    __tablename__ = 'Games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    save_date= Column(DateTime)
    user = relationship('User')
    state = Column(JSON)