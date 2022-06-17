import unittest
class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("inside the setupclass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("inside the tear down class")
    def setUp(self):
        print("inside setup")
    def tearDown(self):
        print("inside the teaerdown")
    def test1(self):
        print("inside the test11")
    def test2(self):
        print("inside the test2")
if __name__=="__main__":
    unittest.main()
