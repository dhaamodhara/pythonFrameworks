from selenium import webdriver
#from Scenario.testing import read
#from Scenario.testing import testing
# data = {"name": "dhamodharan", "ph": '0123456789', "delivery": "Oct. 14, 2021, 4 p.m.",
#         "product_promo": "-0.0","Vat Price": "32.7", "Gross Sale":"500.0", "Pre-VAT Total Sales":"551.3", "Shipping Price":'84.0', "Net Sales":'584.0',
#         "Address":"nye bye Sansiri Condominium,333/553 SoiKruthonbri 1/3, Klongsan Bangkok 10600"}

def asserting_():
    driver = webdriver.Chrome("E:\python_project\First_task\Scenario\chromedriver.exe")
    driver.get("https://shopster.ai/en/login/")
    driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shopstertest")
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("shopster123!")
    driver.find_element_by_xpath("//button[text()='Log into Shopster']").click()
    driver.find_element_by_xpath("//div[text()='Orders']").click()

    driver.find_element_by_xpath("//body[@class='colored-body-style']").click()
    time.sleep(3)
    driver.find_element_by_xpath("(//div[@class='orderer-name'])[4]").click()
    #driver.find_element_by_xpath("(//div[@class='orderer-name'])[5]").click()
l=driver.find_elements_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr")
print(len(l))

a=driver.find_element_by_xpath("(//div[@class='value'])[1]")
print(type(a))
print(f'order is placed by {a.text}')
if a.text == data['name']:
    print("pass")
element = driver.find_element_by_xpath("(//div[@class='value'])[7]")
print(f'order will be delivered by {element.text}')
if element.text == data["delivery"]:
    print("pass")
else:
    print("fail")
element = driver.find_element_by_xpath("(//div[@class='value'])[12]")
print(f'your mobile number is {element.text}')
if element.text == data['ph']:
    print("pass")
else:
    print('fail')
keys = ["product_promo","Vat Price" ]
a=driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Product Promo']/following-sibling::td[last()]")
if data["product_promo"] == a.text:
    print("Product promo is passed")
else:
    print("product promo is failed")
a = driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Vat Price']/following-sibling::td[last()]")
if data["Vat Price"] == a.text:
    print("vat price is passed")
else:
    print("vat price is failed")
a=driver.find_element_by_xpath("//b[text()='500.0']")
if data["Gross Sale"] == a.text:
    print(f"Gross sale is {a.text} test is passed")
else:
    print("Gross sale is not present")
a=driver.find_element_by_xpath("//b[text()='551.3']")
if data["Pre-VAT Total Sales"] == a.text:
    print(f"pre-VAT total sales is {a.text} test is passed")
else:
    print("pre-VAT is not present")
a=driver.find_element_by_xpath("//td[text()='84.0']")
if data['Shipping Price'] == a.text:
    print(f"shipping price is charged {a.text} test is passed")
a=driver.find_element_by_xpath("//b[text()='584.0']")
if data["Net Sales"] == a.text:
    print(f"Net sale amount is {a.text} test is passed")
else:
    print("Net sale is having issue")
image = driver.find_element_by_tag_name('img')
if image:
    print("image is uploaded successfully")
else:
    print("image is not available")
a=driver.find_element_by_xpath("//div[text()='nye bye Sansiri Condominium,333/553 SoiKruthonbri 1/3, Klongsan Bangkok 10600']")
if data["Address"] == a.text:
    print("Address is matched")
else:
    print("Address is not matched")





#ele= driver.find_element_by_xpath("//div[text()='//div[text()='Dhamodharan']"


#a=driver.find_element_by_xpath("(//div[@class='value'])[1]").gettext()
#asserting(data)
#a=driver.find_element_by_xpath("//table[@class='uk-table uk-table-small uk-table-striped']/tbody/tr[*]/td[text()='Points Used']/following-sibling::td[last()]")
# a=driver.find_element_by_xpath("//b[text()='Net Sales']")
# print(a.text)

