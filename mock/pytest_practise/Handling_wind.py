from selenium import webdriver
import time
# chromeoption=webdriver.ChromeOptions()
# chromeoption.add_argument("--disable-notifications")
driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
driver.get("https://www.redbus.in/")

#Write a script to open demowebshop site, click on Facebook link present at the bottom of the webpage.
# Close Facebook browser window opened in new tab
#driver.find_element_by_xpath("//a[text()='Facebook']").click()
# driver.find_element_by_xpath("//button[text()='Try it']").click()
# print(driver.switch_to.alert.text)