# from POM.LoginPage import LoginPage
from Data.ExcelLib import read_locators
from selenium import webdriver
from http import HTTPStatus
import pytest
@pytest.mark.parametrize("username, password", [("u1", "p1"),("u2", "p2")])
class TestLoginPage:

    # def test_enter_email(self):
    #     driver.find_element_by_xpath("//input[@id='username']").send_keys("tomsmith")
    #     driver.find_element_by_xpath("//input[@id='password']").send_keys("SuperSecretPassword!")
    #     driver.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']").click()
    #     actual = driver.current_url
    #     print(actual)
    #     expected="http://the-internet.herokuapp.com/secure"
    #     if actual == expected:
    #         print("Pass")
    #     else:
    #         print("Failed")
    #
    # def test_alpha(self):
    #     driver.get("http://the-internet.herokuapp.com/inputs")
    #     result = driver.find_element_by_xpath("//input[@type='number']").send_keys("abc")
    #     assert True
    #
    # @pytest.mark.regression
    # def test_sorting(self):
    #     driver.get(" http://the-internet.herokuapp.com/tables")
    #     s=driver.find_elements_by_xpath("//table[@id='table1']")
    #     print(type(s))
    #
    #     for item in sorted(s):
    #         print(item.text)
    # @pytest.mark.dependency()
    # def test_indep(self):
    #     print("inependency is running")
    #     assert True
    # @pytest.mark.dependency(depends=["TestLoginPage::test_indep"])
    # def test_dep(self):
    #     print("depencency is running")
    def test_para(self, username, password):
        print("entering", username)
        print("entering", password)
    def test_para2(self, username, password):
        print("entering", username)
        print("entering", password)

# lp=TestLoginPage
# lp.test_enter_email(TestLoginPage)
# lp.test_alpha(LoginPage)
# lp.test_sorting(LoginPage)
# lp.test_image(LoginPage)