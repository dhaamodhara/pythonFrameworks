from gmailproject.setting import driver
class Forward():
    def gmailApp():
        url1=r'https://www.gmail.com'
        url2=r'https://www.flipkart.com/'
        driver.get(url1)
        currenturl=driver.current_url
        print("url",currenturl)
        driver.get(url2)
        currenturl=driver.current_url
        print("url2",currenturl)
        driver.back()
        driver.forward()
        driver.refresh()
        print("finish")
        driver.close()
obj=Forward()
Forward.gmailApp(obj)