from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
import time

driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")

driver.get("file:///E:/Github/Standard_listbox2.html")

# web_elelment=driver.find_element_by_xpath("//select[@id='standard_cars']")
#
# s=Select(web_elelment)
# s.select_by_visible_text('BMW')
#
# time.sleep(2)
#
# s.select_by_index(3)
# time.sleep(3)
#
# s.select_by_value("4")
# time.sleep(2)

lst_sort_by = driver.find_element_by_id("multiple_cars")
s=Select(lst_sort_by)
data=s.options
# items=[item.text for item in data]
# for index, item in enumerate(items):
#     if "BMW" == item:
#         print(f'{item} is present in the index {index}')

print(s.is_multiple)
# try:
#     s.select_by_index(4)
# except StaleElementReferenceException:
#     lst_sort_by=driver.find_element_by_id("products-orderby")
#     s=Select(lst_sort_by)
#     s.select_by_visible_text("Price: High to Low")
# Print the text of all the items present in the listbox

