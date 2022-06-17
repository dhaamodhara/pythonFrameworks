import pytest
#@pytest.mark.skip
def setup():
    print("inside the setup method")
class Test_logout():
    #@pytest.mark.skip(reason="abc")
    def test_login(self):
        print("inside the login method")
    @pytest.mark.skip(reason="mot created")
    def test_logout(self):
        print("inside the logout method")
    @pytest.mark.tryfirst()
    def test_1(self):
        print("inside the try first")
