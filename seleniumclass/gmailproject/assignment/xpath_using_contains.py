from gmailproject.setting import driver,urls
import time
class Assignment():
    def __init__(self):
        print("inside the init methode")
    def gmail(self):
        driver.get(urls["url1"])
        googlelogin="//input[contains(@class,'whsOnd zHQkBf')]"
        driver.find_element_by_xpath(googlelogin).send_keys("username")
        driver.find_element_by_xpath("//span[contains(@class,'RveJvd snByac')]").click()
        #driver.close()
    def flipkart(self):
        driver.get(urls["url2"])
        flipkartsearch="//input[contains(@class,'LM6RPg')]"
        driver.find_element_by_xpath(flipkartsearch).send_keys("mobiles")
        #driver.find_element_by_xpath("//div[starts-with(@class,'_2aUbKa')]").click()
        #driver.find_element_by_xpath("//a[starts-with(@class,'_3ko_Ud'')]").click()
        #time.sleep(2)
        #driver.close()
    def amazon(self):
        driver.get(urls["url3"])
       # amazon_search="https://www.amazon.in/"
        driver.find_element_by_xpath("//input[contains(@id,'twotabsearchtextbox')]").send_keys("earphones")
        time.sleep(2)
        driver.close()
g1=Assignment()
g1.gmail() # calling method by using class name
g1.flipkart() # calling method by using class name
g1.amazon() # calling method by using object name

