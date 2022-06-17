#get screenshot as png
from gmailproject.setting import driver,urls
def gmail():
    driver.get(urls["url1"])
    driver.maximize_window()
    result=driver.get_screenshot_as_png()
    fileobj=open("login.png",'wb')
    fileobj.write(result)
    fileobj.close()
    print(result)
    driver.close()
gmail()