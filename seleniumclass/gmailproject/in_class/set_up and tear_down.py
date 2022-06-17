import unittest
class test(unittest.TestCase):
    @classmethod
    def setUp(self) :
        print("setup is executing")
    @classmethod
    def tearDown(self) :
        print("teardown executing")
    @classmethod
    def setUpClass(cls):
        print("setup class is executing")
    @classmethod
    def tearDownClass(cls):
        print(" teardown class executing")
    def test_asearch(self):
        print("test1 function is executing")
    def test_sdvancedsearch(self):
        print("test 2 function is executing")
if __name__=="__main__":
    unittest.main()