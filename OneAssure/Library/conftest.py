from Library import *

import pytest
from pytest import fixture
@pytest.fixture()
def init(request): #request is an object that hold the information of the fun or class from where the fixture is being called
    driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://staging-app.oneassure.in/page/login")
    driver.maximize_window()
    print(request.cls)
    #cls is the name of the class from wherer init fixrture is being called
    request.cls.driver = driver
    yield
    #driver.quit()
