from selenium import webdriver
driver=webdriver.Chrome("E:\python_project\mock\chromedriver.exe")
driver.get("http://www.yahoo.com")
elements = driver.find_elements_by_name("spam")
texts = ['Hello', 'World']

for element, text in zip(elements, texts):
    element.send_keys(text)






