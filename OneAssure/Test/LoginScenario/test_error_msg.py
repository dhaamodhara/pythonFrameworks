import pytest
from Library.conftest import init
from POM.Loginpage import Login_page
@pytest.mark.usefixtures("init")
class Test_Error:
    def test_Error_Msg(self):
        lp = Login_page(self.driver)
        lp.click_login()