from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.utils import *

def before_all(context):
    driver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver.exe')
    context.service = Service(driver_path)

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=context.service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.carpeta_con_timestamp = crear_carpeta_con_timestamp()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

def after_all(context):
    if hasattr(context, 'service'):
        context.service.stop()







