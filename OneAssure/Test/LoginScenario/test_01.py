from Library import conftest
from Library.conftest import init
from selenium import webdriver
from Library import *
import pytest
from pytest import fixture
@pytest.mark.usefixtures("init")
class Test:
    def test_login(self):
        print("running sucessfully")


