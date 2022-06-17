from Data.ExcelLib import read_locators
from selenium import webdriver
from http import HTTPStatus
import pytest
driver=webdriver.Chrome("E:\python_project\Assignment\Library\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/login")
class TestLoginPage:

    def test_image(self):
        driver.get("http://the-internet.herokuapp.com/broken_images")
        count = driver.find_elements_by_tag_name("img")
        print(len(count))
        if HTTPStatus.OK == 200:
            print("pass")


    def test_enter_email(self):
        driver.find_element_by_xpath("//input[@id='username']").send_keys("tomssmith")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("SuperSecretPasswordd!")
        driver.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']").click()
        actual = driver.current_url
        print(actual)
        expected="http://the-internet.herokuapp.com/secure"
        if actual == expected:
            print("Pass")
        else:
            print("Failed")

    def test_alpha(self):
        driver.get("http://the-internet.herokuapp.com/inputs")
        result = driver.find_element_by_xpath("//input[@type='number']").send_keys("abc")
        assert True
    def test_sorting(self):
        driver.get(" http://the-internet.herokuapp.com/tables")
        s=driver.find_elements_by_xpath("//table[@id='table1']")
        print(type(s))

        for item in sorted(s):
            print(item.text)

    def test_notification(self):
        driver.get(" http://the-internet.herokuapp.com/notification_message_rendered")
        driver.find_element_by_xpath("//a[text()='Click here']").click()

# lp=LoginPage
# lp.enter_email(LoginPage)
# lp.test_alpha(LoginPage)
# lp.test_sorting(LoginPage)
# lp.test_image(LoginPage)

    def test_image(self):
        driver.get("http://the-internet.herokuapp.com/broken_images")
        count = driver.find_elements_by_tag_name("img")
        print(len(count))
        if HTTPStatus.OK == 200:
            print("pass")

    def test_notification(self):
        driver.get(" http://the-internet.herokuapp.com/notification_message_rendered")
        driver.find_element_by_xpath("//a[text()='Click here']").click()