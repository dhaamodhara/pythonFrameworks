import pytest
def test_int_add(a, b):
    return a+b
valid_data = [(1, 2, 3), (10, 20, 30)]
@pytest.mark.parametrize("a, b, expected", valid_data )
def test_valid_int(a, b, expected):
    print(a)
    print(b)
    print(expected)
    assert test_int_add(a, b) == expected
# from selenium import webdriver
# driver= webdriver.Chrome("E:\python_project\First_task\Scenario\chromedriver.exe")
# driver.get("https://shopster.ai/en/login/")
# e=driver.find_element_by_xpath("//td[text()='Bulk Discounts']")
# print(e.text)