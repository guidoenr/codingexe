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
    alias = Column(String(3), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    # string representation of this object
    def __repr__(self):
        return f"<Coin name={self.name} alias={self.alias}>"

def init():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def create_coin(name:str, alias:str):
    coin = Coin(name=name, alias=alias)
    print(coin)
    session.add(coin)
    session.commit()

create_coin('1231', 'ast')
create_coin('213', 'asr')
create_coin('512512', 'ase')
