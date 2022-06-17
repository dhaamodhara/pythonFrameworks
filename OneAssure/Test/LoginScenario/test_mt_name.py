import pytest
from Library.conftest import init
from POM.Loginpage import Login_page
from Data.ExcelLib import read_data
headers, data = read_data("LoginData", "test_01")
@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class Test_Name:
    def test_name(self, username, password, invalid_username, invalid_password ):
        lp = Login_page(self.driver)
        lp.enter_pwd(password)
        lp.click_login()