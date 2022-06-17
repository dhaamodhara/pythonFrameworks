from Data.ExcelLib import read_data
import pytest
from POM.RegisterPage import Test_RegisterPage
from selenium import webdriver
import xlrd
from pytest import mark
from Library.conftest import init
from Library import *
headers, data = read_data("LoginData", "test_01")
print("printg", headers)
print("print", data)
@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class Test_registration:
    def test_reg(self, username, password, invalid_username, invalid_password):

        lp = Test_RegisterPage(self.driver)
        lp.click_reg()