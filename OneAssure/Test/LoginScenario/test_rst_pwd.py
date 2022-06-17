from POM.Loginpage import Login_page
import pytest
from Library.conftest import init
@pytest.mark.usefixtures("init")
class Test_pwd:
    def test_rst_pwd(self):
        lp = Login_page(self.driver)
        lp.click_rst_pwd()