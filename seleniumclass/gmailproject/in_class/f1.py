from gmailproject.setting import driver,urls
from gmailproject.in_class.f2 import Loginpage
class LoginTest():
    def validLogin(self):
        driver.maximize_window()
        driver.get(urls["url1"])
        objlp=Loginpage(driver)
        objlp.login("dhamua459@gmail.com","openmail")
obj=LoginTest()
obj.validLogin()
