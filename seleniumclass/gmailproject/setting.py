from selenium import webdriver
chromepath=r'E:\python_project\seleniumclass\gmailproject\drivers\chromedriver.exe'#copy absolute path
driver = webdriver.Chrome(chromepath)
urls={"url1":"https://www.gmail.com","url2":"https://www.flipkart.com/","url3":"https://www.amazon.in/","url4":"https://www.actitime.com/"}

