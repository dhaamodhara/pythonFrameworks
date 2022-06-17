from selenium import webdriver
import time
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--disable-notifications")

driver=webdriver.Chrome(r'E:\python_project\mock\chromedriver.exe', options=chrome_option)
driver.get("http://www.python.org")
time.sleep(2)

_releases = ['Python 3.7.8', 'Python 3.8.3', 'Python 2.7.17']

for _release in _releases:
    _xpath = f"//a[text()='{_release}']/../..//a[text()=' Download']"
    print(driver.find_element_by_xpath(_xpath).text)
    time.sleep(1)
#driver.get("https://www.indiatoday.in/")
#a=driver.find_element_by_xpath("//header[@id='header']")
# elements=driver.find_elements_by_xpath("/
#
# /div[@class='hmbseindicestable show']//a[text()='S&P BSE Sensex']/../..//li")
# for item in elements:                                                         //a[text()='S&P BSE Sensex']/../..
#     print(item.text)
# i=driver.find_elements_by_xpath("(//td[text()='Karnataka']/..)[1]")
# for item in i:
#     print(item.text)

# driver.switch_to.alert.dismiss()

