from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
driver.get("file:///E:/Github/Double_Click.html")
ele=driver.find_element_by_xpath("//button[text()='Double-click me']")

action=ActionChains(driver)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
#about=driver.find_element_by_xpath("//a[text()='About']")
#blog=driver.find_element_by_xpath("//a[text()='Blog']")
#obj.move_to_element(about).perform()
#obj.move_to_element(blog).perform()
#driver.close()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
def _wait(func):
    def wrapper(*args, **kwargs):
        w=WebDriverWait(driver)
        w.until(ec.visibility_of_element_located)
        func(*args, **kwargs)
    return wrapper
@_wait
def enter_text():
    print("running enter text")
from selenium.webdriver.support.select import Select
driver.window_handles