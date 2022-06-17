from selenium import webdriver
from Data.ExcelLib import read_locators
from Library.generic import SeleniumWrapper
# These are all POM functions
class Login_page(SeleniumWrapper):
    LoginPage_Objects = read_locators("login")

    # def __init__(self, driver):
    #     self.driver = driver
    #     super().__init__(driver)

    def enter_data(self, username):
        locator = Login_page.LoginPage_Objects['PhNo_fld']
        self.enter_text(locator, value = username)

    def enter_pwd(self, data):
        locator = Login_page.LoginPage_Objects['Pwd_fld']
        self.enter_text(locator, value=data)

    def click_login(self):
        locator = Login_page.LoginPage_Objects['Login_btn']
        self.click_element(locator)

    def click_reg(self):
        locator = Login_page.LoginPage_Objects['lnk_register']
        self.click_element(locator)
    def click_rst_pwd(self):
        locator = Login_page.LoginPage_Objects['lnk_reset_pwd']
        self.click_element(locator)


