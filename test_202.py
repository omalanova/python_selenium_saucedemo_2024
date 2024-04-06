import time

from selenium.webdriver.common.by import By
from locators import CART


# ТС-202. Удаление товара из корзины через корзину
        # PreCondition:
        # Пользователь авторизован
        # Корзина не пуста

    # 1. Открыть Корзину
    # 2. Кликнуть "Remove"
    # 3. Проверить, что товар удален из Корзины

def test_202(browser, auth):

    # Add a product in the cart and go there
    browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    browser.find_element(*CART).click()
    time.sleep(1)

    # Remove a product from the cart
    browser.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack').click()

    # Assert the cart is empty
    assert 'shopping_cart_badge' not in browser.page_source
