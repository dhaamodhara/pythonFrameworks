import pytest
@pytest.fixture(autouse=True)
def init():
    print("fixture is running")
    yield
    print("closed")
