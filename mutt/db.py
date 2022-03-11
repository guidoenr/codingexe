from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime 
import logger
import connect


Base = declarative_base()
#engine = create_engine(url, echo=True)

class Coin(Base):
    __tablename__='coin'
    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    # string representation of this object
    def __repr__(self):
        return f"<Coin name={self.name}>"

if __name__ == '__main__':
    engine = connect.get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
