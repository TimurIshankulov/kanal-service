import sys
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Record
from config import conn_string

# Create engine and DBSession instance
engine = create_engine(conn_string)
DBSession = sessionmaker(bind=engine)


class PersistentManager:
    """
    PersistantManager could save table to the database,
    remove missing rows from the database.
    """
    def __init__(self, table):
        self.table = table

    def save(self):
        """Saves records from table to the database"""
        if self.table is None:
            return

        db_session = DBSession()
        for row in self.table:
            while len(row) < 4:
                row.append(None)
            if row[3] is not None:
                row[3] = datetime.datetime.strptime(row[3], '%d.%m.%Y').date()

            record = db_session.query(Record).filter_by(record_id=row[0]).first()
            if record is None:  # Create new record if it doesn't exist
                record = Record(record_id=row[0], order_id=row[1],
                                usd_cost=row[2], shipment_date=row[3])
                db_session.add(record)
            else:  # Update otherwise
                record.order_id = row[1]
                record.usd_cost = row[2]
                record.shipment_date = row[3]
            try:
                db_session.commit()  # Commit changes
            except Exception:
                print(sys.exc_info()[1])
                db_session.rollback()
        db_session.close()

    def remove_missing(self):
        """Removes missing records from the database"""
        if self.table is None:
            return

        db_session = DBSession()
        ids_in_table = [int(row[0]) for row in self.table]
        ids_in_database = db_session.query(Record.record_id).all()
        ids_in_database = [record_id[0] for record_id in ids_in_database]  # Convert to flat list
        ids_to_remove = [x for x in ids_in_database if x not in ids_in_table]

        for id_to_remove in ids_to_remove:
            record = db_session.query(Record).filter_by(record_id=id_to_remove).first()
            db_session.delete(record)
            try:
                db_session.commit()  # Commit deletion
            except Exception:
                print(sys.exc_info()[1])
                db_session.rollback()
        db_session.close()


