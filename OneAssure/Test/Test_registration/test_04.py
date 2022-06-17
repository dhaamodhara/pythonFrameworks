from POM.RegisterPage import Test_RegisterPage
import pytest
from Library.conftest import init
from pytest import mark
from Library import *
from POM.RegisterPage import Test_RegisterPage
from Data.ExcelLib import read_data
headers, data = read_data("RegistrationData", 'test_01')
@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class Test_reg2:
    def test_11ph_num(self, username, password, invalid_username, digit_11_username):
        rp = Test_RegisterPage(self.driver)
        rp.click_reg()
        rp.enter_data(int(digit_11_username))
        rp.click_otp_btn()
