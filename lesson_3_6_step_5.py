import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]
@pytest.mark.parametrize('url', url_list)
def test_guest_should_see_login_link(browser, url):
    link = url
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR,
                         ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys("XXXXXX@gmail.com")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("XXXXXXXX")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()
    WebDriverWait(browser, 1).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".light-tabs.ember-view"))
    )

    try:
        browser.find_element(By.CSS_SELECTOR, ".again-btn.white").click()
    except:
        text_area = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
        text_area.send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        ".svg-icon.correct_icon.ember-view.attempt-wrapper__result-icon"))
    )
    result = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    result_text = result.text
    assert result_text == "Correct!", f"Result is incorrect '{result_text}"



