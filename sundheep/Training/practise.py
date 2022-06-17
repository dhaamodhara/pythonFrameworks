from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("file:/E:/Github/Standard_listbox2.html")
list_box=driver.find_element_by_id("standard_cars")
s=Select(list_box)
opts=s.options
print(opts)
for item in opts:
    print(item.text)
s.select_by_visible_text('Mini')
time.sleep(3)