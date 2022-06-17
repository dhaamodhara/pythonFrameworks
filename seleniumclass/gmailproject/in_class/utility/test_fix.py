import pytest
from selenium import webdriver
driver=webdriver.Chrome("")
def test_divisible_by_3(input_value):

   print("running after")
@pytest.mark.parametrize("username,password",[("u1","p1"),("u2","p2")],scope="class")
class Test_Login:
   @pytest.mark.dependency()
   def test_admin(self,username,password):
      print("entering",username)
      print("entering",password)
      assert False
   @pytest.mark.dependency(depends=["Test_Login::test_admin"])
   def test_user ( self, username, password):
      print("entering ",username)
      print("entering",password)
wn_handl=driver.window_handles
driver.switch_to.window()