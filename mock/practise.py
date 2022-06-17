from selenium import webdriver
driver=webdriver.Chrome(r'E:\python_project\mock\chromedriver.exe')
driver.get("file:///E:/Github/Table_Sorting.html")
datas=driver.find_elements_by_xpath("//table[@id='myTable']//td[1]")
expected_result=sorted([item.text for item in datas])
driver.get("file:///E:/Github/Table_Sorting.html")
(driver.find_elements_by_xpath("//button[text()='Sort']"))[0].click()
datas=driver.find_elements_by_xpath("//table[@id='myTable']//td[1]")
Actual_result=[item.text for item in datas]
if expected_result== Actual_result:
    print("pass")
else:
    print("Fail")
