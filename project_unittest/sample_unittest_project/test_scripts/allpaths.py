from selenium import webdriver
chromepath=r'E:\python_project\project_unittest\sample_unittest_project\drivers\chromedriver.exe'
urls={"url1":"https://www.gmail.com","url2":"https://www.flipkart.com/","url3":"https://www.amazon.in/",
      "url4":"https://www.actitime.com/"}
logfilepath=r'E:\python_project\project_unittest\sample_unittest_project\logfiles'
reportpath=r'E:\python_project\project_unittest\sample_unittest_project\reports'
driver=webdriver.Chrome(chromepath)
