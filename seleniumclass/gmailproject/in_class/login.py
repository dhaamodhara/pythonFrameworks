from gmailproject.setting import driver,urls

def display():
    driver.get(urls['url1'])
    driver.close()

display()
