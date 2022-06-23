import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class', autouse=True)
def browser_invocation(request):
    # Chrome Browser Invocation
    s = Service("C:\chromedriver.exe")
    driver = Chrome(service=s)
    driver.maximize_window()

    # Get into Automation practice url
    driver.get('http://automationpractice.com/index.php')

    # assigning the driver to driver of Test_OrderAuto class
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def login_info():
    return {'user_id': 'yeshank.pawar@cbnits.com', 'passwd': 'Pawar@123'}


@pytest.fixture()
def product_info():
    return {'product_name': 'Casual Shirt'}

