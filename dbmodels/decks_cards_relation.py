from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
class DC_rel(Base):
    __tablename__ = 'Deck_cards_relation'

    deck = relationship('Deck')
    card = relationship('Card')