import sys
import xml.etree.ElementTree as ET
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Record
from config import conn_string

cbr_url = 'https://www.cbr.ru/scripts/XML_daily.asp'
# Create engine and DBSession instance
engine = create_engine(conn_string)
DBSession = sessionmaker(bind=engine)


class CurrencyUpdater:
    """
    Class for getting and update quotes and prices.
    Pass the currency you want to get from the CBR to constructor.
    """
    def __init__(self, currency):
        self.currency = currency

    def get_quote(self):
        """Returns quote of stored currency"""
        response = requests.get(cbr_url)
        root = ET.fromstring(response.text)
        currency_list = root.findall('Valute')

        for currency in currency_list:
            if currency.find('CharCode').text == self.currency:
                quote = currency.find('Value').text
                quote = float(quote.replace(',', '.'))  # Value is string with ',' separator
                return quote
        return 0

    def update_rub_currency(self, quote):
        """Updates ruble cost in the database column 'rub_cost'"""
        db_session = DBSession()

        records = db_session.query(Record).all()
        for record in records:
            if record.usd_cost is not None:
                record.rub_cost = round(record.usd_cost * quote, 2)
            else:
                record.rub_cost = None
            try:
                db_session.commit()  # Commit changes
            except Exception:
                print(sys.exc_info()[1])
                db_session.rollback()
        db_session.close()
