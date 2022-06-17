import unittest
from project_unittest.sample_unittest_project.pages.loginPage import LoginPage
from project_unittest.sample_unittest_project.test_scripts.allpaths import driver,urls,logfilepath
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter("%(asctime)s:%(created)f:%(levelname)s:%(filename)s: %(message)s")
filehandler=logging.FileHandler(logfilepath+"loginpage.log")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver.maximize_window()
        driver.get(urls['url1'])
        driver.implicitly_wait(30)
    def test_loginpage(self):
        logger.info("in login page test method")
        obj=LoginPage(driver)
        obj.login("dhamua459@gmail.com","openmail")
        print(driver.title)
    @classmethod
    def tearDownClass(cls):
        logger.info("in tear down class")
        driver.close()
        driver.quit()
        logger.info("app closed")
if __name__=="__main__":
    unittest.main(verbosity=2)

