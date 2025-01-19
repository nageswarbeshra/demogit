
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome"
    )

    parser.addoption(
        "--browser_head", action="store", default="withHead"
    )



@pytest.fixture(scope="class")
def setup(request):
    current_time = datetime.datetime.now()
    browser_name = request.config.getoption("browser_name")
    browser_head = request.config.getoption("browser_head")
    if browser_name == "chrome":
        Chrome_option = ChromeOptions()
        service_obj = ChromeService("C:/Users/nages/PycharmProjects/PythonSelfFramework/resouces/chromedriver.exe")
        if browser_head == "withoutHead":
            Chrome_option.add_argument("--headless")
            driver = webdriver.Chrome(service=service_obj, options=Chrome_option)
            print(f": {current_time} : Test Started in Headless Chrome Browser.....")
        else:
            driver = webdriver.Chrome(service=service_obj, options=Chrome_option)
            print(f": {current_time} : Test Started in Chrome Browser.....")

    elif browser_name == "firefox":
        Firefox_option = FirefoxOptions()
        service_obj = FirefoxService("C:/Users/nages/PycharmProjects/PythonSelfFramework/resouces/geckodriver.exe")
        if browser_head == "withoutHead":
            Firefox_option.add_argument("--headless")
            driver = webdriver.Firefox(service=service_obj, options=Firefox_option)
            print(f": {current_time} : Test Started in Headless Firefox Browser.....")
        else:
            driver = webdriver.Firefox(service=service_obj, options=Firefox_option)
            print(f": {current_time} : Test Started in Firefox Browser.....")

    elif browser_name == "edge":
        Edge_option = webdriver.EdgeOptions()
        if browser_head == "withoutHead":
            Edge_option.add_argument("--headless")
            driver = webdriver.Edge()
            print(f": {current_time} : Test Started in Headless Edge Browser.....")
        else:
            driver = webdriver.Edge()
            print(f": {current_time} : Test Started in Edge Browser.....")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print("\n", current_time, ": Test Completed successfully!")
    driver.close()
