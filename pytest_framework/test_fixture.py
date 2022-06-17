import pytest
@pytest.fixture()
def setup():
    print("inside the setup method")
def test_1(setup):
    print("inside the test 1")
def test_2(setup):
    print("inside the test 2")