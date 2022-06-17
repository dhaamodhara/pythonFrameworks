from Library.conftest import init
import pytest
from POM.Loginpage import Login_page
from Data.ExcelLib import read_data
headers, data = read_data("LoginData", "test_01")
@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class Test_invalid_num:
    def test_num(self, username, password, invalid_username, invalid_password ):
        lp = Login_page(self.driver)
        lp.enter_data('9008109393')
        lp.enter_pwd(password)
        lp.click_login()