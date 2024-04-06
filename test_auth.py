from selenium.webdriver.common.by import By
import time
from locators import *
from data import MAIN_PAGE, LOGIN_FAIL, PASSWORD_FAIL


# TC-101. Авторизация используя корректные данные (standard_user, secret_sauce)

# 1. Открыть url: https://www.saucedemo.com/v1/
# 2. Ввести "standard_user" в "Username"
# 3. Ввести "secret_sauce" в "Password"
# 4. Кликнуть "Login"
# 5. Проверить, что мы перешли на новый url: https://www.saucedemo.com/v1/inventory.html
# 5. Проверить, что имеется текст "Products"

def test_login_form(browser, auth):
    # находим текст в элементе TITLE
    actual_text = browser.find_element(*TITLE).text
    expected_text = "Products"

    # time.sleep(5)
    # assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    assert actual_text == expected_text, f'Unexpected text, expected text: {expected_text}, actual text: {actual_text}'
    time.sleep(5)


# TC-102. Авторизация используя некорректные данные (user, user)

# 1. Открыть url: https://www.saucedemo.com/v1/
# 2. Ввести "user" в "Username"
# 3. Ввести "user" в "Password"
# 4. Кликнуть "Login"
# 5. Проверить, что появляется предупреждение

def test_auth_negative(browser):
    browser.get(MAIN_PAGE)

    browser.find_element(*USERNAME_FIELD).send_keys(LOGIN_FAIL)
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_FAIL)
    browser.find_element(*LOGIN_BUTTON).click()
    time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').is_displayed()
