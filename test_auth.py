from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


#TC-01. Авторизация

    # 1. Открыть url: https://www.saucedemo.com/v1/
    # 2. Ввести "standard_user" в "Username"
    # 3. Ввести "secret_sauce" в "Password"
    # 4. Кликнуть "Login"
    # 5. Проверить, что мы перешли на новый url: https://www.saucedemo.com/v1/inventory.html

def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')
   
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()


#TC-02. Авторизация

    # 1. Открыть url: https://www.saucedemo.com/v1/
    # 2. Ввести "user" в "Username"
    # 3. Ввести "user" в "Password"
    # 4. Кликнуть "Login"
    # 5. Проверить, что появляется предупреждение

def test_auth_negative():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('user')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    assert browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').is_displayed()

    browser.quit()