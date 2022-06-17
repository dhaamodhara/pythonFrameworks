import xlrd
from selenium import webdriver
driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
def read_data(sheetname):
    wb=xlrd.open_workbook(r"C:\Users\Amaresh\Documents\Book1.xls")
    wc=wb.sheet_by_name(sheetname)
    return {item[0].value: item[1].value for item in wc}
a=read_data("Sheet1")
print(a)