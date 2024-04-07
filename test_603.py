import time

from selenium.webdriver.common.by import By


# ТС-603. Проверка работоспособности кнопки "Reset App State" в меню
    # 1. Открыть главную страницу
    # 2. Перейти в меню навигации
    # 3. Выбрать ""Reset App State""
    # 4. Убедиться, что система вернулась в исходное состояние: товары из корзины вернулись в каталог

def test_603(browser, auth):

    # Add t-shirt in the cart
    browser.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()
    cart_badge = browser.find_element(By.CSS_SELECTOR, 'span.shopping_cart_badge')

    # Click on "Burger menu"
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(3)

    # Click on "Reset App State"
    browser.find_element(By.ID, 'reset_sidebar_link').click()

    assert cart_badge not in browser.find_elements(By.CLASS_NAME, 'shopping_cart_link'), 'error'