import os
import traceback

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'secret.json'


class GoogleSpreadsheetFetcher:
    """
    Class works with Google Spreadsheets.
    Fetches data from the spreadsheet and generate table - a list of lists.
    Specify spreadsheet_id to work with.
    Call get_table() to receive the results.
    """

    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    @staticmethod
    def get_service():
        """Returns builded service"""
        try:
            creds, _ = google.auth.default()
            service = build('sheets', 'v4', credentials=creds)
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
        return service

    def get_table(self):
        """Returns table with content loaded from Google Spreadsheet"""
        ranges = []
        include_grid_data = True
        service = self.get_service()
        try:
            request = service.spreadsheets().get(spreadsheetId=self.spreadsheet_id, ranges=ranges,
                                                 includeGridData=include_grid_data)
            response = request.execute()
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

        table = []
        data = response['sheets'][0]['data'][0]['rowData']
        for i in range(len(data)):
            row = []
            for j in range(len(data[i]['values'])):
                if j < 4:
                    row.append(data[i]['values'][j].get('formattedValue'))
            table.append(row)
        if len(table) > 1:
            print('Data fetched successfully')
            return table[1:]
        else:
            return None

