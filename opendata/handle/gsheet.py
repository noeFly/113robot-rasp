from pandas import DataFrame
from pygsheets import authorize
from toolBox import getTime


def writeSheet(dataID: str, rawData):
    gCloud = authorize(service_account_file='./creative-113-f58c5c386088.json')
    gSheet = gCloud.open_by_key('1oOXiGIKsZaeckzPxZSUjAzNiLEC5CgEnqusLuRHMfao')
    if dataID == 'O-A0002-002':
        workSheet = gSheet.worksheet_by_title('openData')
        value: list = [getTime(), dataID]
        for i in rawData:
            value.append(i)
        workSheet.append_table(values=value, dimension='ROWS')


# create empty dataframe
dFrame = DataFrame()
