#save screenshot
from gmailproject.setting import driver,urls
def screenshot():
    driver.get(urls["url1"])
    driver.maximize_window()
    driver.save_screenshot("log.png")
    driver.close()
screenshot()