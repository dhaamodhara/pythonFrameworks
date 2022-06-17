from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from Scenario.second_scenario import asserting_
import time
from selenium.webdriver.common.action_chains import ActionChains

def order_page():
    data = {"name": "dhamodharanA", "ph": '0123456789', "Address":"ABC Colony,xyz district- 10600", "date":'14'}
    # , "delivery": "Oct. 14, 2021, 4 p.m.",
    #             "product_promo": "-0.0","Vat Price": "32.7", "Gross Sale":"500.0", "Pre-VAT Total Sales":"551.3", "Shipping Price":'84.0', "Net Sales":'584.0',
    #                  "Address":"nye bye Sansiri Condominium,333/553 SoiKruthonbri 1/3, Klongsan Bangkok 10600"}
    #
    driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://rollingpinn.shopster.ai/en/")
    # driver.switch_to.default_content()
    driver.find_element_by_xpath("//body[@style='overflow-y: scroll;']").click()
    time.sleep(3)
    # driver.find_element_by_xpath("//body[@class='fixed']").click()
    #driver.find_element_by_class_name('all-products-single-name with-collection').click()
    actions = ActionChains(driver)
    actions.send_keys('\ue00f').perform()
    time.sleep(3)
    driver.find_element_by_xpath("(//img[@class='with-collection'])[24]").click()
    #driver.find_element_by_xpath("(//img[@class='with-collection'])[6]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Add to bag']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='profile-icon checkout']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//i[@id='signupClose']").click()
    driver.find_element_by_xpath("//span[@class='checkout-chatbot-choices-single']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='chat-input']").send_keys(data["name"])
    driver.find_element_by_xpath("//i[@class='material-icons chat-send']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='chat-input']").send_keys(data["ph"])
    driver.find_element_by_xpath("//i[@class='material-icons chat-send']").click()
    time.sleep(1)
    driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='chat-input']").send_keys(data["Address"])
    driver.find_element_by_xpath("//i[@class='material-icons chat-send']").click()
    time.sleep(2)
    driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[1]").click()
    driver.find_element_by_xpath("//span[@class='checkout-chatbot-choices-single']").click()
    time.sleep(1)
    driver.find_element_by_xpath(f"//td[text()={data['date']}]").click()
    driver.find_element_by_xpath("//input[@id='timealone']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[@class='rolldate-btn rolldate-confirm']").click()
    driver.find_element_by_xpath("(//td[text()='30'])[2]").click()
    driver.find_element_by_xpath("//input[@id ='timealone']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[@class='rolldate-btn rolldate-confirm']").click()
    driver.find_element_by_xpath("//span[@class='checkout-chatbot-choices-single']").click()
    time.sleep(1)
    driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='payment-input']").send_keys(r"C:\Users\Amaresh\Downloads\Flower.jpg")
    time.sleep(20)
    #data["vat"] = driver.find_element_by_class_name("vat-price").text
    driver.find_element_by_xpath("//span[text()='Yes, it is']").click()
    time.sleep(5)
    confirmation = driver.find_element_by_xpath("//div[@class='checkout-chatbot-bubble'][@data-stage='complete']").text
    order_id = confirmation.split('Order #')[1].split('\n')[0]
    data['order_id'] = order_id
    a=driver.find_element_by_xpath("(//div[text()='Subtotal for 1 items']/..//div)[2]").text
    if a[0] == '฿' and a[1] == ' ' :
        data["Sub_total"] = float(a[2:])
    a = driver.find_element_by_xpath("(//div[text()='Shipping Price']/..//div)[4]").text
    if a[0] == '฿' and a[1] == ' ':
        data["shipping_price"] = float(a[2:])
    a= driver.find_element_by_xpath("(//div[text()='Pre-VAT Total']/..//div)[16]").text
    if a[0] == '฿' and a[1] == ' ':
        data["Pre-VAT_total"] = float(a[2:])
    a= driver.find_element_by_xpath("(//div[text()='VAT 7%']/..//div)[18]").text
    if a[0] == '฿' and a[1] == ' ':
        data["VAT"] = float(a[2:])
    a = driver.find_element_by_xpath("(//div[text()='Total']/..//div)[22]").text
    if a[0]== '฿' and a[1] == ' ':
        data["Total"] = float(a[2:])
    print(data)
    time.sleep(11)
    return data

def asserting(data):
    driver = webdriver.Chrome("E:\python_project\OneAssure\Library\chromedriver.exe")
    driver.get("https://shopster.ai/en/login/")
    driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shopstertest")
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("shopster123!")
    driver.find_element_by_xpath("//button[text()='Log into Shopster']").click()
    driver.get(f"https://shopster.ai/en/app/orders/{data['order_id']}/")
    # driver.find_element_by_xpath("//div[text()='Orders']").click()
    # driver.find_element_by_xpath(f"//a[@data-id='{data['order_id']}'").click()
    a = driver.find_element_by_xpath("(//b[text()='Gross Sales']/../..//td)[3]").text
    print(a)
    if data["Sub_total"] == float(a):
        print(f"Gross sale amount is {data['Sub_total']} test is passed")
    else:
        print("Gross sale amount is not matched")
    a = driver.find_element_by_xpath("(//b[text()='Pre-VAT Total Sales']/../..//td)[3]").text
    print(a)
    if order_result["Pre-VAT_total"] == float(a):
        print(f"Pre VAT total is {data['Pre-VAT_total']} test is passed")
    else:
        print("Pre-VAT amount is not matched")
    a = driver.find_element_by_xpath("(//td[text()='Shipping Price']/..//td)[3]").text
    if order_result["shipping_price"] == float(a):
        print(f"Shipping Price is {data['shipping_price']} test is passed")
    else:
        print("shipping price is not matched")
    a =driver.find_element_by_xpath("(//td[text()='Vat Price']/..//td)[3]").text
    if order_result["VAT"] == float(a):
        print(f"The VAT price is {data['VAT']} test is passed")
    else:
        print("VAT price is not matched")
    a = driver.find_element_by_xpath("(//b[text()='Net Sales']/../..//td)[3]").text
    if order_result["Total"] == float(a):
        print(f"Total amount is {data['Total']} test is passed")
    else:
        print("Total is not matched")

# order_result = order_page()
#order_result={'name': 'dhamodharanA', 'h': '0123456789', 'Address': 'ABC Colony,xyz district- 10600', 'date': '14', 'Sub_total': '฿ 220', 'shipping_price': '฿ 68', 'Pre-VAT_total': '฿ 232.49', 'VAT': '฿ 11.51', 'Total': '฿ 244.00'}
# print(order_result)
# asserting(order_result)
time.sleep(100.0)
# driver.find_element_by_xpath("//body[@class='colored-body-style']").click()
# time.sleep(3)
# driver.find_element_by_xpath("(//div[@class='orderer-name'])[4]").click()
# #driver.find_element_by_xpath("(//div[@class='orderer-name'])[5]").click()
# l=driver.find_elements_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr")
# print(len(l))
# time.sleep(3)
# actions = ActionChains(driver)
# actions.send_keys('\ue00f').perform()
# time.sleep(3)
# #data["vat"] = driver.find_element_by_xpath("//div[@class='total-right vat-price']").text
# data["vat"] = driver.find_element_by_xpath("//td[text()='32.7']").text
# #data["total"] = driver.find_element_by_xpath("//div[@class='total-right total-price']").text
# data["total"] = driver.find_element_by_xpath("//b[text()='584.0']").text
# data["product_promo"] = driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Product Promo']/following-sibling::td[last()]").text
# data["Vat Price"] = driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Vat Price']/following-sibling::td[last()]").text
# data["Gross Sale"] = driver.find_element_by_xpath("//b[text()='500.0']").text
# data["Pre-VAT Total Sales"] = driver.find_element_by_xpath("//b[text()='551.3']").text
# data['Shipping Price'] = driver.find_element_by_xpath("//td[text()='84.0']").text
# data["Net Sales"] = driver.find_element_by_xpath("//b[text()='584.0']").text
# data["Address"] = driver.find_element_by_xpath("//div[text()='nye bye Sansiri Condominium,333/553 SoiKruthonbri 1/3, Klongsan Bangkok 10600']").text
#
# a=driver.find_element_by_xpath("(//div[@class='value'])[1]")
# print(type(a))
# print(f'order is placed by {a.text}')
# if a.text == data['name']:
#     print("pass")
# element = driver.find_element_by_xpath("(//div[@class='value'])[7]")
# print(f'order will be delivered by {element.text}')
# # if element.text == data["delivery"]:
# #     print("pass")
# # else:
# #     print("fail")
# element = driver.find_element_by_xpath("(//div[@class='value'])[12]")
# print(f'your mobile number is {element.text}')
# if element.text == data['ph']:
#     print("pass")
# else:
#     print('fail')
# keys = ["product_promo","Vat Price" ]
# a=driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Product Promo']/following-sibling::td[last()]")
# if data["product_promo"] == a.text:
#     print("Product promo is passed")
# else:
#     print("product promo is failed")
# a = driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Vat Price']/following-sibling::td[last()]")
# if data["Vat Price"] == a.text:
#     print("vat price is passed")
# else:
#     print("vat price is failed")
# a=driver.find_element_by_xpath("//b[text()='500.0']")
# if data["Gross Sale"] == a.text:
#     print(f"Gross sale is {a.text} test is passed")
# else:
#     print("Gross sale is not present")
# a=driver.find_element_by_xpath("//b[text()='551.3']")
# if data["Pre-VAT Total Sales"] == a.text:
#     print(f"pre-VAT total sales is {a.text} test is passed")
# else:
#     print("pre-VAT is not present")
# a=driver.find_element_by_xpath("//td[text()='84.0']")
# if data['Shipping Price'] == a.text:
#     print(f"shipping price is charged {a.text} test is passed")
# a=driver.find_element_by_xpath("//b[text()='584.0']")
# if data["Net Sales"] == a.text:
#     print(f"Net sale amount is {a.text} test is passed")
# else:
#     print("Net sale is having issue")
# image = driver.find_element_by_tag_name('img')
# if image:
#     print("image is uploaded successfully")
# else:
#     print("image is not available")
# a=driver.find_element_by_xpath("//div[text()='nye bye Sansiri Condominium,333/553 SoiKruthonbri 1/3, Klongsan Bangkok 10600']")
# if data["Address"] == a.text:
#     print("Address is matched")
# else:
#     print("Address is not matched")
# print(data)





#driver.find_element_by_xpath("(//span[@class='checkout-chatbot-choices-single'])[2]").click()
#driver.find_element_by_xpath("//span[text()='Yes, it is']").click()
#time.sleep(5)

