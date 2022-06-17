from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://rollingpinn.shopster.ai/en/")
# driver.find_element_by_xpath("//body[@style='overflow-y: scroll;']").click()
# actions = ActionChains(driver)
# actions.send_keys('\ue00f').perform()
# time.sleep(2)
# color_of_text = driver.find_element_by_xpath("//div[@class='filter active']").value_of_css_property('color')
# if color_of_text == "rgba(0, 255, 0, 1)":
#     print("color of the text is matched")
# else:
#     print("color of the text is not matched")
# img = driver.find_element_by_xpath("//div[@class='logo']")
# if img.is_displayed():
#     print("Logo is visible in webpage")
# else:
#     print("Logo is not present in th web page")
driver.get("https://shopster.ai/en/app/dashboard/")
driver.get("https://shopster.ai/en/login/")
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shopstertest")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("shopster123!")
driver.find_element_by_xpath("//button[text()='Log into Shopster']").click()
driver.find_element_by_xpath("(//div[@class='tab-text'])[4]").click()
driver.find_element_by_xpath("//span[text()='Store Design']").click()
driver.find_element_by_xpath("//span[text()='Colors']").click()
driver.find_element_by_xpath("(//div[@class='pcr-swatches ']//button)[3]").click()
driver.find_element_by_xpath("//input[@aria-label='save and close']").click()
# #Font
driver.find_element_by_xpath("//span[text()='Fonts']").click()
driver.find_element_by_xpath("//div[text()='Acumin Pro']").click()
driver.find_element_by_xpath("//span[text()='Save']").click()
# #Logo
driver.find_element_by_xpath("//span[text()='Logo']").click()
driver.find_element_by_xpath("//input[@id='id_logo']").send_keys(r"C:\Users\Amaresh\Downloads\Logo.png")
driver.find_element_by_xpath("//span[@id='save']").click()

# a=driver.find_element_by_xpath("//div[@id='filter-110']")
# a.click()
# colour = Color.from_string(driver.find_element_by_xpath("//div[@id='filter-110']").value_of_css_property('color'))
# csss = a.value_of_css_property("color")
# assert colour.rgba == 'rgba(0, 0, 0, 0.54)'

# element = driver.find_element_by_xpath("(//div[text()='The Rolling Pinn'])[2]")
# style = element.get_attribute('style')
# print(style)

# rgb = driver.find_element_by_xpath("//div[@id='filter-110']").value_of_css_property('background-color')
# hex = Color.from_string(rgb).hex
# print