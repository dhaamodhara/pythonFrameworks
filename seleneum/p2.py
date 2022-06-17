import time
from selenium import webdriver
driver =webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximum_window()
driver.minimum_window()
driver.fullscreen_window()
time.sleep(2)
print("The curent url page is",driver.current_url)
driver.back()
driver.forward()
driver.refresh()
print("The title is",driver.title)
driver.close