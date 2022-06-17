import pytest

@pytest.fixture(autouse=True,  scope="class")
def func(request):
    print("func is running")
    def teardown():
        print("taerdown method is running")
    request.addfinalizer(teardown)

class TestFixture:
    def test_01(self):
        print("test_01 is running")
    def test_02(self):
        print("test_02 is running")
class Test02:
    def test_c2(self):
        print("test_c2")
