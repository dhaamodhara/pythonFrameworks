import unittest
import HtmlTestRunner
class Test_prg(unittest.TestCase):
    def test_login(self):
        print("in login from:",__name__)
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Report'))