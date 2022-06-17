from selenium import webdriver
import time
driver=webdriver.Chrome('E:\python_project\mock\chromedriver.exe')
# driver.get("http://demowebshop.tricentis.com/")
driver.get("https://www.naukri.com/")
# driver.find_element_by_xpath("//input[@name='keyword']").send_keys("python")
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Search']").click()
# time.sleep(5)
#links=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
links=driver.window_handles
for link in links:
    driver.switch_to.window(link)
    time.sleep(1)
    print(driver.title)

#links[0].click()
handles=driver.window_handles
print("----------",handles)
time.sleep(1)
driver.switch_to.window(handles[1])
driver.find_element_by_xpath("//button[@id='logToApp']").click()
# driver.find_element_by_xpath("//a[text()='Twitter']").click()
# handles=driver.window_handles # to get all the wind handles
# driver.switch_to.window(handles[1])
# time.sleep(1)
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hi hello")
# time.sleep(2)
#driver.switch_to.window(handles[0])