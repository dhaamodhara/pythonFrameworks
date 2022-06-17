from gmailproject.setting import driver,urls
from selenium.webdriver.support.select import Select
file=r'E:\python_project\seleniumclass\gmailproject\in_class\dropdown.html'
def selectdrop():
    driver.get(file)
    element='//select[@id="subject"]'
    obj=driver.find_element_by_xpath(element)
    s=Select(obj)
    s.select_by_index(3)
    obj1=driver.find_element_by_id("checkbox").click()
    obj1.isselected()
    print(obj1)
selectdrop()
