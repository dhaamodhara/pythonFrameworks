import unittest as ut
from gmailproject.setting import driver,urls
class Test_login(ut.TestCase):
    def testgmail(self):
        driver.implicitly_wait(10)
        driver.get(urls["url1"])
        username=r'//input[@id="identifierId"]'
        loginbtn=r'//span[text()="Next"]'
        driver.find_element_by_xpath(username).send_keys("admin")
        driver.find_element_by_xpath(loginbtn).click()
        #driver.find_element_by_xpath(password).send_keys("password")
        #driver.find_element_by_xpath.().click()
        driver.close()
    def test_actitime(self):
        driver.implicitly_wait(10)
        driver.get(urls["url4"])
        username=r'//input[@id="username"]'
        password=r'//input[@name="pwd"]'
        loginbtn=r'//div[text()="Login "]'
        driver.find_element_by_xpath(username).send_keys("admin")
        driver.find_element_by_xpath(password).send_keys("manager")
        driver.find_element_by_xpath(loginbtn).click()
        driver.close()
if __name__=="__main__":
    ut.main()