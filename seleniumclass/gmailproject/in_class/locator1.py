from gmailproject.setting import driver,urls
from selenium.webdriver.common.by import By
def display():
    driver.get(urls["url1"])
    driver.find_element_by_id("identifierId").send_keys("abc")
    #driver.find_element_by_class_name("RveJvd snByac").click()
    import time
    driver.find_element_by_css_selector("span[class='RveJvd snByac']").click()
    #time.sleep(3)
    #driver.find_element_by_css_selector('input[class="whsOnd zHQkBf"][name="password"]').send_keys("12345")
    driver.find_elements_by_tag_name('span').click()
    #driver.find_element(By.TAG_NAME,'button').click()
   # driver.find_element_by_partial_link_text("Forgot password")
   # driver.find_element_by_tag_name()
   # driver.find_element_by_name()
   # driver.close()
    print('finish')
display()