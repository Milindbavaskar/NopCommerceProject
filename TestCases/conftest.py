import pytest
from selenium.webdriver.edge import webdriver
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Edge()
    driver.get("https://admin-demo.nopcommerce.com")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Firefox()
        #driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(params=[("admin@yourstore.com","admin","Pass"),
                        ("admin@yourstore.com","admin1","Fail"),
                        ("admin@yourstore.com1","admin","Fail"),
                        ("admin@yourstore.com1","admin1","Pass")])

def getDataforLogin(request):
    return request.param