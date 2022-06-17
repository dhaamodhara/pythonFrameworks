import xlrd
path=r'C:\Users\Amaresh\Documents\loginpage.xls'
def read_locators(sheetname):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name(sheetname)
    r = worksheet.get_rows()
   # next(r) #skipping the header
    return {item[0].value:item[1].value for item in r}

read_locators('loginpage')
