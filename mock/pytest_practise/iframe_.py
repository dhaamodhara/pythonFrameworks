from selenium import webdriver
import time
chromeoption=webdriver.ChromeOptions()
chromeoption.add_argument("--disable-notification")
driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe", options=chromeoption)
driver.get("file:///E:/Github/iframe.html")
time.sleep(2)
driver.switch_to.frame("frame1")
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Business']").click()