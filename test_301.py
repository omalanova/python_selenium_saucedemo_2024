import time

from selenium.webdriver.common.by import By

    # ТС-301. Добавление товара в корзину через каталог
        # 1. Открыть главную страницу
        # 2. Перейти в каталог товаров из меню навигации
        # 3. Кликнуть на картинку товара
        # 4. Проверить, что мы перешли в карточку товара

def test_adding_product_to_cart(browser, auth):
    browser.find_element(By.ID, 'item_4_img_link').click()
    time.sleep(1)

    # находим текст на странице
    actual_text = browser.find_element(By.ID, 'back-to-products').text
    expected_text = "Back to products"

    assert actual_text == expected_text, f'Unexpected text, expected text: {expected_text}, actual text: {actual_text}'