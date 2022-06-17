from selenium.webdriver.common.action_chains import ActionChains
from selenium import  webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
driver.get("file:///E:/Github/Double_Click.html")
ele=driver.find_element_by_xpath("//button[text()='Double-click me']")
o=ActionChains(driver)
o.double_click(ele).perform()
e=WebDriverWait(driver, time=10)
e.until(ec.visibility_of())