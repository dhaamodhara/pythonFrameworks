from selenium import webdriver
driver = webdriver.Chrome("E:\python_project\First_task\Scenario\chromedriver.exe")
driver.get("https://shopster.ai/en/app/dashboard/")
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shopstertest")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("shopster123!")
driver.find_element_by_xpath("//button[text()='Log into Shopster']").click()
driver.find_element_by_xpath("(//div[@class='tab-text'])[4]").click()
driver.find_element_by_xpath("(//span[@class='store-menu-text'])[5]").click()
driver.find_element_by_xpath("//i[@class='material-icons']").click()
driver.find_element_by_xpath("//input[@class='uk-input']").send_keys("Sweet Candies")
driver.find_element_by_xpath("//option[text()='MILK CANDY']").click()
driver.find_element_by_xpath("//option[text()='Test phone bundle 2']").click()
driver.find_element_by_xpath("//span[@id='save']").click()
