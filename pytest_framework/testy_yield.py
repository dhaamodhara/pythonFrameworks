import  pytest
@pytest.yield_fixture()

def setup():
    print("inside the setup method")
    print("before methods")
    yield
    print("after every test method")
def test1(setup):
    print("inside the test11")
def test2(setup):
    print("inside the test22")
