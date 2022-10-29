from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class Games(Base):
    __tablename__ = 'Games'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable= False)
    save_date= Column(DateTime, nullable= False)
    user = relationship('User')
    state = Column(JSON, nullable= False)