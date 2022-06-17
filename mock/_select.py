from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver= webdriver.Chrome(r'E:\python_project\mock\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com/books")
time.sleep(2)


_books = ['Science', 'Health Book', 'Fiction', 'Computing and Internet']

for _book in _books:
    _xpath = "//a[text()='{}']/../..//input[@value='Add to cart']".format(_book)
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(1)


driver.find_element_by_xpath("//span[@class='close']").click()
driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
#driver.find_element_by_partial_link_text("Shopping cart").click()

_book = "Fiction"
_checkbox=("//a[text()='Fiction'])[2]/../..//input[@name='removefromcart']")
driver.find_element_by_xpath("//a[text()='Fiction'])[2]/../..//input[@value=1585658]").click()
driver.find_element_by_xpath("(//a[text()='Fiction'])[2]/../..//input[@name='removefromcart']").click()
driver.find_element_by_xpath("//input[@name='updatecart']").click()

#_checkbox = f"(//a[text()='{_book}'])[2]/../..//input[@name='removefromcart']"
#driver.find_element_by_xpath(_checkbox).click()
from selenium.webdriver.common.action_chains import ActionChains
actions=ActionChains(driver)
actions.move_to_element(loc)