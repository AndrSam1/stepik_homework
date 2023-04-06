import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: safari or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "safari":
        print("\nstart firefox browser for test..")
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome or safari")
    yield browser
    print("\nquit browser..")
    browser.quit()