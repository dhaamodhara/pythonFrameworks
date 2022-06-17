
import time
from project_unittest.sample_unittest_project.test_scripts.allpaths import driver,urls
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    _username='//input[@id="identifierId"]'
    _nextBtn='//span[text()="Next"]'
    _password ="//input[@name='password']"
    _loginBtn="//span[text()='Next']"
    def getusername(self):
        return driver.find_element_by_xpath(self._username)
    def nextbtn(self):
        return driver.find_element_by_xpath(self._nextBtn)
    def getpassword(self):
        return driver.find_element_by_xpath(self._password)
    def loginbtn(self):
        return driver.find_element_by_xpath(self._loginBtn)
    def enterusername(self,user):
        self.getusername().send_keys(user)
    def clicknext(self):
        self.nextbtn().click()
    def enterpassword(self,pwd):
        self.getpassword().send_keys(pwd)
    def clickloginbtn(self):
        self.loginbtn().click()
    def login(self,username,password):
        self.enterusername(username)
        self.clicknext()
        self.enterpassword(password)
        time.sleep(4)
        self.clickloginbtn()







