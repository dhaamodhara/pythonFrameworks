from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("file:/E:/Github/Standard_listbox2.html")
# def enter_text(locator,value):
#     locator_type,locator_value=locator
#     driver.find_element(locator_type,locator_value).clear()
#     driver.find_element(locator_type,locator_value).send_keys(value)
# def click_element(locator):
#     locator_type,locator_value=locator
#     driver.find_element(locator_type,locator_value).click()
def select_item(locator,*,item):
    locator_type,locator_value=locator
    lst_box=driver.find_element(locator_type,locator_value)
    s=Select(lst_box)
    opts=[opt.text for opt in s.options]
    print(opts)
    if isinstance(item,str):
        if item not in opts:
            raise ValueError(f'{item} is not present in list')
        s.select_by_visible_text(item)
    else:
        s.select_by_index(item)
def select_items(locator,*,items):
    for item in items:
        try:
            select_item(locator,item=item)
            time.sleep(1)
        except (ValueError,IndexError):
            print(f'({item} is not present in the list box')
            continue
    # locator_type,locator_value=locator
    # lst_box=driver.find_element(locator_type,locator_value)
    # s=Select(lst_box)
    # for item in items:
    #     if isinstance(item,str):
    #         s.select_by_visible_text(item)
    #         time.sleep(1)
    #     else:
    #         s.select_by_index(item)

select_items(("id",'multiple_cars'),items=["Hnda","Ford",7])

#enter_text(('name','q'),"computer")
#click_element(fin("xpath","//a[text()='Register']"))
# driver.find_element_by_xpath("//a[text()='Register']").click()
#click_element(("xpath","//input[@id='gender-male']"))
# driver.find_element_by_xpath("//input[@id='gender-male']").click()
#enter_text(("x#path","//input[@id='FirstName']"),"dhamo")
#enter_text(("xpath","//input[@id='LastName']"),"dharan")
#click_element(("xpath","//input[@name='register-button']"))
# driver.find_element_by_xpath("//input[@id='FirstName']").send_keys("dhamo")
# driver.find_element_by_xpath("//input[@id='LastName']").send_keys("dharan")
# driver.find_element_by_xpath("//input[@name='register-button']").click()