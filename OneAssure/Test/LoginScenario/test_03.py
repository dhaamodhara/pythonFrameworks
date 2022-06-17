from Data.ExcelLib import read_data
import pytest
from Library import *
import xlrd
from Library.conftest import init
from selenium import webdriver
from POM.Loginpage import Login_page
from pytest import mark
from Data.ExcelLib import read_data
from POM.Loginpage import Login_page

# Read headers and test data in list of tuples
headers, data = read_data("LoginData", "test_01")
print("printing headers", headers)
print("printing data", data)
#_driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class TestLogin:
    def test_login(self, username, password, invalid_username, invalid_password ):
        print("printing test_login")
        print("printing username", username)
        print("printing password", password)
        lp = Login_page(self.driver)
        # Enter Phone number
        lp.enter_data('9008109357')
        lp.click_login()

# from Data.ExcelLib import read_data
# import pytest
# from Library import *
# import xlrd
# from Library.conftest import init
# from selenium import webdriver
# from POM.Loginpage import Login_page
# from pytest import mark
# from Data.ExcelLib import read_data
# from POM.Loginpage import Login_page
#
# headers, data = read_data('LoginData', 'test_01')
# import pytest
# @pytest.mark.usefixtures("init")
# @pytest.mark.parametrize(headers, data)
# class Test_valid_data:
#     def test_ph_number(self, number, password):
#         lp = Login_page(self.driver)
#         lp.enter_data(number)