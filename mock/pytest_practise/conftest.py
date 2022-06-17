import pytest
# @pytest.fixture(autouse=True)
# def init():
#     print("launching url")
#     yield
#     print("closing the browser")
@pytest.fixture(scope="session")
def init():
    print("navigating url")
    yield
    print("closing browser")