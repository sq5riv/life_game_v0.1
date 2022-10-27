from sqlalchemy import Column, Integer, String, JSON, LargeBinary
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Card(Base):
    __tablename__ = 'Cards'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(Integer)
    new_in_hand_action = Column(String)  # Action performed when card comes to hand
    rotation_condition = Column(String)
    normal_desc = Column(JSON)
    rotate_desc = Column(JSON)
    icon = Column(LargeBinary)

