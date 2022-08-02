from sqlalchemy import Column, Integer, String, BLOB, Float, Boolean, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import conn_string

DeclarativeBase = declarative_base()
# Create engine and DBSession instance
engine = create_engine(conn_string)
DBSession = sessionmaker(bind=engine)

db_session = DBSession()


class Record(DeclarativeBase):
    """
    Class describes record in table. Each record is a row in table.
    """
    def __init__(self, record_id, order_id, usd_cost, shipment_date):
        self.record_id = record_id
        self.order_id = order_id
        self.usd_cost = usd_cost
        self.shipment_date = shipment_date
        self.rub_cost = None

    # ====== Table options ====== #

    __tablename__ = 'orders'

    record_id = Column(Integer(), primary_key=True, nullable=False)
    order_id = Column(Integer())
    usd_cost = Column(Float())
    shipment_date = Column(Date())
    rub_cost = Column(Float())


DeclarativeBase.metadata.create_all(engine)
DeclarativeBase.metadata.bind = engine
