from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime 
import logger, connect

Base = declarative_base()
engine, session = connect.get_engine_and_session()

class Coin(Base):
    __tablename__='coins'
    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    symbol = Column(String(3), nullable=False, unique=True)
    homepage = Column(String(30))
    hashing_algorithm = Column(String(20), default='None')
    price_change_24h = Column(Integer())


    def __repr__(self):
        return f"<Coin name={self.name} alias={self.alias}>"

def init():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

init() # TODO esto