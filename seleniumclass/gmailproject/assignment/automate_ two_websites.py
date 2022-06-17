from gmailproject.setting import driver,urls,url2
import time
class Css_selector():
    def display():
        driver.get(urls["url1"])
        driver.find_element_by_css_selector("input[id='identifierId']").send_keys("dhamua459@gmail.com")
        driver.find_element_by_css_selector("span[class='RveJvd snByac']").click()
        currenturl=driver.current_url
        time.sleep(2) #because below line need time to enter the data
        driver.find_element_by_css_selector("input[class='whsOnd zHQkBf'][type='password']").send_keys("password")
        driver.get(url2["url2"])
        currenturl1=driver.current_url
        driver.find_element_by_css_selector("input[class='LM6RPg']").send_keys("mobiles")
        driver.find_element_by_class_name("_2fcmoV").click()
        dict={"gmail":currenturl,"flipkart":currenturl1}
        print(dict)
        driver.close()
object=Css_selector()
object.display()