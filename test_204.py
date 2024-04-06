import time

from selenium.webdriver.common.by import By

# ТС-204. Добавление товара в корзину из карточки товара
    # 1. Открыть главную страницу сайта
    # 2. Перейти в карточку товара, нажав на его название
    # 3. Добавить товар в Корзину, нажав на кнопку "Add to cart"
    # 4. Кликнуть "Remove"
    # 5. Название кнопки "Remove" меняется на "Add to cart"
    # 5. Проверить, что товар удален из Корзины

def test_204(browser, auth):

    # Add a product in the cart and go there
    browser.find_element(By.ID, 'item_4_title_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    time.sleep(1)

    # Remove a product from the cart
    browser.find_element(By.CSS_SELECTOR, '#remove').click()

    # Assert the cart is empty
    assert 'shopping_cart_badge' not in browser.page_source