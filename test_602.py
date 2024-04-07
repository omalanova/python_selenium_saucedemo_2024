import time

from selenium.webdriver.common.by import By


# ТС-602. Проверка работоспособности кнопки "About" в меню
    # 1. Открыть главную страницу
    # 2. Перейти в меню навигации
    # 3. Выбрать "About"
    # 4. Убедиться, что осуществлен переход на сайт saucelabs.com

def test_602(browser, auth):

    # Click on "Burger menu"
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(3)

    # Click on "About"
    browser.find_element(By.ID, 'about_sidebar_link').click()
    time.sleep(3)

    assert browser.current_url == 'https://saucelabs.com/'
    assert "The world relies on your code. Test on thousands of different device, browser, and OS configurations–anywhere, any time." in browser.page_source