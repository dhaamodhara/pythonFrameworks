from gmailproject.setting import driver,urls
def gmailApp():

    driver.get(urls['url1'])
    driver.maximize_window()
    driver.minimize_window()
    driver.close()
    print("finish")
gmailApp()
