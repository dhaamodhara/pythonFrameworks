import os
class Config:

    project_dir = os.getcwd().split('Tests')[0]
    data_file_path = r'C:\Users\Amaresh\Documents\TestDatas.xls'
    objects_file_path = r'C:\Users\Amaresh\Documents\Copy of objects.xls'

    URL = 'https://staging-app.oneassure.in/page/login'
    BROWSER_NAME = "chrome"
    USERNAME = ""
    PASSWORD = ""
    FIREFOX_DRIVER_PATH = r""
    GECKO_DRIVER_PATH = r""
    CHROME_DRIVER_PATH = "../Library/chromedriver"
    IE_DRIVER_PATH = r""
    DATA_FILE_PATH = data_file_path
    OBJECTS_FILE_PATH = objects_file_path