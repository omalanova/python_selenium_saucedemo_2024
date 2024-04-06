import time

from selenium.webdriver.common.by import By

# ТС-203. Добавление товара в корзину из карточки товара
    # 1. Открыть главную страницу сайта
    # 2. Войти в каталог товаров из меню навигации
    # 3. Перейти в карточку товара нажав название товара
    # 4. Нажать на кнопку "Add to cart"
    # 5. Проверить, что выбранный товар добавлен в корзину.
    # 6. Перейти в корзину для проверки добавленного товара.

def test_203(browser, auth):

    # Add a product in the cart and go there
    browser.find_element(By.ID, 'item_4_title_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    time.sleep(1)

    # Assert the product is in the cart
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').is_displayed()