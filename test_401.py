import time

from selenium.webdriver.common.by import By

from faker import Faker

# ТС-401. Оформление заказа используя корректные данные
    # 1. Открыть главную страницу
    # 2. Перейти в каталог товаров из меню навигации
    # 3. Добавить товар в корзину
    # 4. Перейти в Корзину
    # 5. Нажать кнопку ""Checkout""
    # 6. Ввести фейковые данные для оформления заказа
    # 7. Нажать кнопку Finish
    # 8. Отображается надпись "Thank you for your order!"

fake = Faker("ru_Ru")
def test_401(browser, auth):

    # Add a product in the cart
    browser.find_element(By.ID, 'item_4_img_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    # proceed to Checkout
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    browser.find_element(By.ID, 'checkout').click()
    # fill out the form fields
    browser.find_element(By.ID, "first-name").send_keys(fake.first_name())
    browser.find_element(By.ID, 'last-name').send_keys(fake.last_name())
    browser.find_element(By.ID, 'postal-code').send_keys(fake.postcode())
    # complete the order
    browser.find_element(By.CSS_SELECTOR, "[name='continue']").click()
    browser.find_element(By.CSS_SELECTOR, "[name='finish']").click()

    assert "Thank you for your order!" in browser.page_source