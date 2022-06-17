# import xlrd
# import pytest
# wb=xlrd.open_workbook(r'C:\Users\Amaresh\Documents\Book1.xls')
# rows=wb.sheet_by_name("Sheet1")
# a=rows.get_rows()
# for index, item in enumerate(a):
#     #print(index)
#     print(item)
#     if not item[0].value == "test_01":
#         continue
#     headers=rows.row_values(index-1, start_colx=1)
#     print(headers)
# # print(type(a))d
# # for item in a:
# #     print(item)
# @pytest.mark.parametrize("username, password",[("u1", "p1"), ('u2', 'p2')])
# class Test_:
#     def test_l(self,username, password):
#         print("entering",username)
#         print("entering", password)
import time
from selenium import webdriver
#driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
# driver.get("https://money.rediff.com/index.html")
# s=driver.find_elements_by_xpath("//div[@class='hmtable1']")
# print(s)
# for i in s:http://demowebshop.tricentis.com/
#     print(i.text)
#Print the link text of all the links in python.org iff the linktext contains word 'Python' in it.
# Also, print the attribute 'href' of the corresponding link.
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
driver = webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
from selenium.webdriver.support.select import Select
driver.get("file:///E:/Github/iframe.html")
driver.switch_to.frame()