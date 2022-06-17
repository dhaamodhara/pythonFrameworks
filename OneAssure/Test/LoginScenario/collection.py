from selenium import webdriver
# driver = webdriver.Chrome("E:\python_project\First_task\Scenario\chromedriver.exe")
# driver.get("https://shopster.ai/en/app/dashboard/")
# driver.get("https://shopster.ai/en/login/")
# driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shopstertest")
# driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("shopster123!")
# driver.find_element_by_xpath("//button[text()='Log into Shopster']").click()
# driver.find_element_by_xpath("(//div[@class='tab-text'])[4]").click()
# driver.find_element_by_xpath("(//span[@class='store-menu-text'])[5]").click()
# driver.find_element_by_xpath("//i[@class='material-icons']").click()
# driver.find_element_by_xpath("//input[@class='uk-input']").send_keys("verydelicious Candies")
# driver.find_element_by_xpath("//option[text()='MILK CANDY']").click()
# driver.find_element_by_xpath("//option[text()='Test phone bundle 2']").click()
# driver.find_element_by_xpath("//span[@id='save']").click()

from selenium.webdriver.common.action_chains import ActionChains
def test():
    datas = {"collection_name":'verydelicious-candies'}
    driver = webdriver.Chrome("E:\python_project\First_task\Scenario\chromedriver.exe")
    driver.get("https://rollingpinn.shopster.ai/en/")
    driver.find_element_by_xpath("//body[@style='overflow-y: scroll;']").click()
    import time
    time.sleep(3)
    print(f" collection is printing{datas['collection_name']}")
    actions = ActionChains(driver)
    actions.send_keys('\ue010').perform()

    # element=f"//h2[@id={datas['collection_name']}]"
    # a=driver.find_element_by_xpath(element)
    a=driver.find_element_by_xpath(f"//h2[@id='verydelicious-candies']")
    # driver.find_element_by_xpath("//h2[@id='sweet-candies']").click()
    # a=driver.find_element_by_xpath("//h2[@id='sweety-candies-1']")
    if a:
        print("collection is present")
    else:
        print("collection is not present")
        import time
        time.sleep(2)
    # a=driver.find_element_by_xpath("(//h3[@class='all-products-single-name with-collection'])[51]").text
    # a=driver.find_element_by_xpath("(//div[@data-id='714'])[14]").text
    a=driver.find_element_by_xpath("(//div[@class='horizontal-products-container'])[23]").text
    print(a)
    if a.startswith("MILK CANDY"):
        print("product name is matched")
    else:
        print("product name is not matched")
    # driver.find_element_by_xpath("(//img[@class='with-collection'])[52]").click()
test()