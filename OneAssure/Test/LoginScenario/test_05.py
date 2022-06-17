from selenium import webdriver
import time
driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
driver.get("https://shopster.ai/en/app/dashboard/")
driver.get("https://shopster.ai/en/login/")
# driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shopstertest")
# driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("shopster123!")
# driver.find_element_by_xpath("//button[text()='Log into Shopster']").click()
# driver.find_element_by_xpath("(//a[@class='custom-link tab-item '])[3]").click()
# driver.find_element_by_xpath("//span[text()='Products']").click()
# driver.find_element_by_xpath("//i[text()='add']").click()
# driver.find_element_by_xpath("//div[text()='Add Product']").click()
# driver.find_element_by_xpath("(//input[@class='uk-input'])[1]").send_keys("Honey Cake")
# driver.find_element_by_xpath("//div[@name='description']").send_keys("Sweet and Delecious")
# driver.find_element_by_xpath("//select[@name='category']").click()
# driver.find_element_by_xpath("//option[@value='114']").click()
# driver.find_element_by_xpath("//option[@value='bike']").click()
# driver.find_element_by_xpath("//input[@id='original-price-input']").send_keys("100")
# driver.find_element_by_xpath("//input[@id='is-discount-enabled']").click()
# driver.find_element_by_xpath("//input[@name='discounted-price']").send_keys("10")
# driver.find_element_by_xpath("//span[@class='add-image-text']").click()
# driver.find_element_by_xpath("//button[@id='upload-from-phone']").click()
# driver.find_element_by_xpath("//input[@id='phone-input']").send_keys(r"C:\Users\Amaresh\Downloads\HoneyCake.jpg")
# # driver.find_element_by_xpath("//input[@id='has-message']").click()
# driver.find_element_by_xpath("//input[@name='has_note']").click()
# driver.find_element_by_xpath("//input[@name='has_file']").click()
# driver.find_element_by_xpath("//input[@name='has_reference_file']").click()
# driver.find_element_by_xpath("//span[@id='save']").click()

from selenium.webdriver.common.action_chains import ActionChains
def asserting():
    data = {"name": "Honey Cake", "price": "100", "description": "Sweet and Delecious", "discount":"10"}
    driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://rollingpinn.shopster.ai/en/")
    driver.find_element_by_xpath("//body[@style='overflow-y: scroll;']").click()
    actions = ActionChains(driver)
    actions.send_keys('\ue00f').perform()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='search-input-box']").send_keys("Honey Cake")
    driver.find_element_by_xpath("(//img[@class='with-collection'])[59]").click()
    product_name = driver.find_element_by_xpath("//h2[@class='banner-text banner-text-left']").text
    print("printing name", product_name)
    if data['name'] == product_name:
        print(f"Name of the {product_name} is passed")
    else:
        print("name of the product is not matched")
    price = driver.find_element_by_xpath("//span[@class='banner-text banner-text-right-strike']").text
    print(price)
    if price[0] == '฿' and price[1] == ' ' :
        price = price[2:]
    if data['price'] == price:
        print(f"price of the product is {price} test is passed")
    else:
        print("price of the product is not matched ")
    discount = driver.find_element_by_xpath("//span[@class='banner-text banner-text-right']").text
    if discount[0] == '฿' and discount[1] == ' ' :
        discount = discount[2:]
    if data['discount'] == discount:
        print(f"discount orice of the product {discount} and test is passed")
    else:
        print("discount price is not matched")
    description = driver.find_element_by_xpath("//div[@class='product-desc']").text
    if data['description'] == description:
        print(f"description of the product is {description} and test is passed ")
    # driver.find_element_by_xpath("//button[text()='Add to bag']").click()
    #
    # driver.find_element_by_xpath("//a[@class='profile-icon checkout']").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//i[@id='signupClose']").click()
    # driver.find_element_by_xpath("//span[@class='checkout-chatbot-choices-single']").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//input[@id='chat-input']").send_keys(data["name"])
    # driver.find_element_by_xpath("//i[@class='material-icons chat-send']").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//input[@id='chat-input']").send_keys(data["ph"])
    # driver.find_element_by_xpath("//i[@class='material-icons chat-send']").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[1]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[2]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//input[@id='chat-input']").send_keys(data["Address"])
    # driver.find_element_by_xpath("//i[@class='material-icons chat-send']").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[1]").click()
    # driver.find_element_by_xpath("//span[@class='checkout-chatbot-choices-single']").click()
    # time.sleep(1)
    # driver.find_element_by_xpath(f"//td[text()={data['date']}]").click()
    # driver.find_element_by_xpath("//input[@id='timealone']").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//span[@class='rolldate-btn rolldate-confirm']").click()
    # driver.find_element_by_xpath("(//td[text()='30'])[2]").click()
    # driver.find_element_by_xpath("//input[@id ='timealone']").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//span[@class='rolldate-btn rolldate-confirm']").click()
    # driver.find_element_by_xpath("//span[@class='checkout-chatbot-choices-single']").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[2]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//input[@id='payment-input']").send_keys(r"C:\Users\Amaresh\Downloads\Flower.jpg")
    # time.sleep(20)
    # # data["vat"] = driver.find_element_by_class_name("vat-price").text
    # driver.find_element_by_xpath("//span[text()='Yes, it is']").click()
    # time.sleep(5)
asserting()
time.sleep(40)