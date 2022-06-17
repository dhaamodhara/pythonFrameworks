import time
from selenium.webdriver.common.by import By
class Loginpage():
    def __init__(self,driver):
        self.driver=driver
    _username="//input[@id='identifierId']"
    _nextBtn="//div[@class='ZFr60d CeoRYc']"
    _password="//input[@name='password']"
    _loginBtn="//span[text()='Next']"
    def getusername(self):
        return self.driver.find_element(By.XPATH,self._username)
    def nextbtn(self):
        return self.driver.find_element(By.XPATH,self._nextBtn)
    def getpassword(self):
        return self.driver.find_element(By.XPATH,self._password)
    def loginbtn(self):
        return self.driver.find_element(By.XPATH,self._loginBtn)
    def enterusername(self,user):
        self.getusername().send_keys(user)
    def clicknext(self):
        self.nextbtn().click()
    def enterpassword(self,pwd):
        self.getpassword().send_keys(pwd)
    def clicklogin(self):
        self.loginbtn().click()
    def login(self,username,password):
        self.enterusername(username)
        self.clicklogin()
        time.sleep(4)
        self.enterpassword(password)
        time.sleep(4)
        self.clicklogin()
        title=self.driver.title
        print(title)
