from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


# Если вы теперь запустите тесты без параметра, то получите ошибку:
#
# pytest -s -v test_parser.py
# _pytest.config.UsageError: --browser_name should be chrome or firefox
# Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
#
# parser.addoption('--browser_name', action='store', default="chrome",
#                  help="Choose browser: chrome or firefox")
# Давайте укажем параметр:
#
# pytest -s -v --browser_name=chrome test_parser.py
# А теперь запустим тесты на Firefox:
#
# pytest -s -v --browser_name=firefox test_parser.py
# Вы должны увидеть, как сначала тесты запустятся в браузере Chrome, а затем — в Firefox.