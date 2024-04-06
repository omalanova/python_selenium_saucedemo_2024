import time

from selenium.webdriver.common.by import By

# ТС-302. Успешный переход к карточке товара после клика на название товара
    # 1. Открыть главную страницу
    # 2. Перейти в каталог товаров из меню навигации
    # 3. Кликнуть на название товара
    # 4. Проверить, что мы перешли в карточку товара"

def test_302(browser, auth):

    # Add a product in the cart and go there
    browser.find_element(By.ID, 'item_4_title_link').click()
    time.sleep(1)

    # находим текст на странице
    actual_text = browser.find_element(By.ID, 'back-to-products').text
    expected_text = "Back to products"

    assert actual_text == expected_text, f'Unexpected text, expected text: {expected_text}, actual text: {actual_text}'