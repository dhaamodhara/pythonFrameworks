import xlrd
from Library.config import Config

def read_data(sheetname, testcase):
    workbook = xlrd.open_workbook(Config.DATA_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    temp_data =[]
    data = []
    header = None
    rows = worksheet.get_rows()
    for index, item in enumerate(rows):
        if not item[0].value == testcase:
            continue
        headers = worksheet.row_values(index - 1, start_colx =2)
        headers = ','.join(headers)
        break
    r = worksheet.get_rows()  # Re-initialising iterator
    for item in r:
        if item[0].value == testcase:
            temp_data.append(tuple([temp.value for temp in item])[1:])
    for d in temp_data:
        if d[0].upper() == 'YES':
            data.append(d[1:])
    return [headers, data]

def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    r = worksheet.get_rows()
    next(r)     # Skip Headers
    return {item[0].value: (item[1].value, item[2].value) for item in r}
