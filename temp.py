import time
from selenium.webdriver.support.select import Select

from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

def test_successful_open_product_card():
    item_id = 5
    browser.get('https://www.saucedemo.com/')
    browser.find_element('css selector', '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()

    browser.find_element(By.ID, f'item_{item_id}_img_link').click()
    assert browser.current_url == f'https://www.saucedemo.com/inventory-item.html?id={item_id}'


def test_checkout():
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    browser.find_element(By.ID, 'item_4_img_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    browser.find_element(By.ID, 'checkout').click()
    browser.find_element(By.ID, "first-name").send_keys('Svetlana')
    browser.find_element(By.ID, 'last-name').send_keys("Zimina")
    browser.find_element(By.XPATH, '//input[@data-test="postalCode"]').send_keys("56789")
    browser.find_element(By.CSS_SELECTOR, "[name='continue']").click()
    browser.find_element(By.CSS_SELECTOR, "[name='finish']").click()
    assert "Thank you for your order!" in browser.page_source


def test_add_item_from_the_card():
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    browser.find_element(By.ID, 'item_4_img_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    time.sleep(3)
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').is_displayed()


def test_filter_z_a():
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()
    select = Select(dropdown)
    select.select_by_index(1)
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_label')
    product_names = [product.text for product in products]
    sorted_product_names = sorted(product_names, reverse=True)
    assert product_names == sorted_product_names, 'что-то не то'


def test_filter_lohi():
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    Select(browser.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value('lohi')
    time.sleep(3)
    prices = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    price_names = [float(price.text[1::]) for price in prices]
    sorted_product_prices = sorted(price_names)
    assert price_names == sorted_product_prices, 'error'


# def test_burger_menu_logout():
#     browser.get(url)
#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#     time.sleep(3)
#     browser.find_element(By.XPATH, '//*[text()="Logout"]').click()
#     time.sleep(3)
#     assert browser.current_url == 'https://www.saucedemo.com/', 'error'
#     browser.quit()
#
#
# def test_burger_menu_repp_app_state():
#     browser.get(url)
#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     browser.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
#     cart_bage = browser.find_element(By.CSS_SELECTOR, 'span.shopping_cart_badge')
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#     time.sleep(3)
#     #page_update = browser.page_source
#     browser.find_element(By.XPATH, '//*[text()="Reset App State"]').click()
#     assert cart_bage not in browser.current_url, 'Ошибка: значок корзины присутствует'

# assert cart_bage not in browser.find_elements(By.CLASS_NAME, 'shopping_cart_link'), 'error'

# browser.quit()


def test_log_out():
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(3)
    browser.find_element(By.ID, 'logout_sidebar_link').click()
    assert browser.current_url == 'https://www.saucedemo.com/'


def test_click_about():
    browser.maximize_window()
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(3)
    browser.find_element(By.ID, 'about_sidebar_link').click()
    assert browser.current_url == 'https://saucelabs.com/'
    assert browser.find_element(By.CSS_SELECTOR, '[src="/images/logo.svg"]').is_displayed()