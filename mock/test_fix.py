from selenium import webdriver
# driver=webdriver.Chrome(r'E:\python_project\mock\chromedriver.exe')
from utility import is_even
import pytest
@pytest.fixture()
def init():
    print("running init")
# @pytest.mark.usefixtures("init")
class Test_utility:
    @pytest.mark.smoke
    def test_even(self,init):
        print("running even")
        is_even(10)

    @pytest.mark.smoke
    def test_odd(self, init):
        print("running odd")
        with pytest.raises(TypeError):
            is_even(1.1)

    @pytest.mark.smoke
    def test_grouping(self, init):
        print("groupiing")