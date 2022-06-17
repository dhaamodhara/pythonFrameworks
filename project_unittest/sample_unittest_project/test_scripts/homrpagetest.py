class HomePage():
    def __init__(self,driver):
        self.driver=driver

    logoutBtn_xpath="//a[text()='Logout']"

    def getlogoutBtn(self):
        return self.driver.find_element_by_xpath(self.logoutBtn_xpath)

    def clicklogout(self):
        self.getlogoutBtn().click()
