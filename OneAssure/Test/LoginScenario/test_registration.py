from Library.conftest import init
from POM.Loginpage import Login_page
import pytest
@pytest.mark.usefixtures("init")
class Test_Registration:
    def test_reg(self):
        lp = Login_page(self.driver)
        lp.click_reg()
