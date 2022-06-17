from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
def _wait(func):
    w=WebDriverWait(driver,timeout=10)
    def wrapper(*args, **kwargs):
        locator,  =args
        w.until(ec.visibility_of_element_located(locator))
        return func(*args, **kwargs)
    return wrapper

@_wait
def enter_text(locator, *, value):
    loc_type, loc_value= locator
    driver.find_element(loc_type, loc_value).clear()
    driver.find_element(loc_type,loc_value).send_keys("hello")

@_wait
def click_element(locator):
    loc_type, loc_value=locator
    driver.find_element(loc_type, loc_value).click()

def select_item(locator, *, item):
    element=driver.find_element_by_xpath()
    s=Select(element)
    opt=s.options
    items=[item.text for item in opt ]
    if isinstance(item, str):
        if item not in items:
            raise ValueError(f'{item} is not present in list box')
        s.select_by_visible_text(item)
    else:
        if item>len(items):
            raise IndexError("index error")
        else:
            s.select_by_index(item)
enter_text(("xpath", "//input[@value='Search store']"), value="Hello")

click_element(("xpath", "//a[text()='Register']"))