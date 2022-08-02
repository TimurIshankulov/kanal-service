import time

from google_spreadsheet_fetcher import GoogleSpreadsheetFetcher
from persistent_manager import PersistentManager
from currency_updater import CurrencyUpdater

SPREADSHEET_ID = '1GhA2pITIdmMIGLfWBh8ApXdFJNxhteuHiABSACsnPVQ'

if __name__ == '__main__':
    while True:
        fetcher = GoogleSpreadsheetFetcher(SPREADSHEET_ID)
        table = fetcher.get_table()

        manager = PersistentManager(table)
        manager.save()
        manager.remove_missing()

        updater = CurrencyUpdater('USD')
        quote = updater.get_quote()
        updater.update_rub_currency(quote)
        time.sleep(5)
