from sqlalchemy import Column, Integer, String, JSON, LargeBinary
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Card(Base):
    __tablename__ = 'Cards'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable= False)
    version = Column(Integer, nullable= False)
    new_in_hand_action = Column(String, nullable= False)  # Action performed when card comes to hand
    rotation_condition = Column(String, nullable= False)
    normal_desc = Column(JSON, nullable= False)
    rotate_desc = Column(JSON, nullable= False)
    icon = Column(LargeBinary, nullable= False)

