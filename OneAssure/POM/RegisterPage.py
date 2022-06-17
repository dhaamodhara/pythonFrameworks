from selenium import webdriver
from Data.ExcelLib import read_locators
from Library.generic import SeleniumWrapper
class Test_RegisterPage(SeleniumWrapper):
    RegisterPage_Objects = read_locators("registration")

    # def __init__(self, driver):
    #     self.driver = driver
    #     super().__init__(driver)

    def enter_data(self, username):
        locator = Test_RegisterPage.RegisterPage_Objects['txt_field']
        self.enter_text(locator, value = username)

    def click_otp_btn(self):
        locator = Test_RegisterPage.RegisterPage_Objects['otp_btn']
        self.click_element(locator)

    def click_reg(self):
        locator = Test_RegisterPage.RegisterPage_Objects['lnk_register']
        self.click_element(locator)

    def click_rst_pwd(self):
        locator = Test_RegisterPage.RegisterPage_Objects['rst_pwd']
        self.click_element(locator)

    def click_back_btn(self):
        locator = Test_RegisterPage.RegisterPage_Objects['back_btn']
        self.click_element(locator)
    #
    # def click_rst_pwd(self):
    #     locator = Login_page.LoginPage_Objects['lnk_reset_pwd']
    #     self.click_element(locator)