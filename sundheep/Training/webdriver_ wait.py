from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec           #ec is a module
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
w=WebDriverWait(driver,10)    # creating a class instance object for a webdriverwait
#ele_fname=driver.find_element("name","fname")
#w.until(ec.visibility_of(ele_fname),message="element could not be loaded") # using until method from webdriverwait class
#w.until(ec.visibility_of_element_located(("name","fname")))
# loader_ele=driver.find_element("id","loader")
# w.until(ec.invisibility_of_element(loader_ele))
#w.until(ec.invisibility_of_element_located(("id","loader")))
#ele_fname.send_keys("supeb")
class element_visiblity_and_enabled:
    def __init__(self,locator):
        self.locator=locator
    def __call__(self,driver):
        loc_type,loc_value=self.locator
        element=driver.find_element(loc_type,loc_value)
        if element.is_enabled and element.is_displayed:
            return True
        else:
            return False
w=WebDriverWait(driver,20)
s=element_visiblity_and_enabled(("name","q"))
w.until(s)
driver.find_element_by_name("q").send_keys("try")


