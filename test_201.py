import time

from selenium.webdriver.common.by import By

    # ТС-201. Добавление товара в корзину через каталог
    # 1. Открыть главную страницу сайта.
    # 2. Перейти в каталог "All items" из меню навигации.
    # 3. Выбрать конкретный товар из каталога.
    # 4. Нажать на кнопку "Add to cart"
    # 5. Проверить, что выбранный товар добавлен в корзину.
    # 6. Перейти в корзину для проверки добавленного товара.

def test_adding_product_to_cart(browser, auth):
    browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').is_displayed()