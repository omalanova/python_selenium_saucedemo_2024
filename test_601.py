import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# ТС-601. Выход из системы
    # 1. Открыть главную страницу
    # 2. Перейти в меню навигации
    # 3. Выбрать ""Logout""
    # 4. Убедиться, что осуществлен выход из системы

def test_601(browser, auth):

    # Click on "Burger menu"
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(3)

    # Click on "Logout"
    browser.find_element(By.ID, 'logout_sidebar_link').click()

    assert browser.current_url == 'https://www.saucedemo.com/'