import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# ТС-503. Проверка работоспособности фильтра (low to high)
    # 1. Открыть главную страницу
    # 2. Перейти в каталог товаров из меню навигации
    # 3. В выпадающем списке выбрать фильтр low to high
    # 4. Убедиться, что товары отсортированы в порядке возрастания цены

def test_503(browser, auth):

    # Click on dropdown
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()

    # Select "Price (low to high)"
    Select(browser.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value('lohi')
    time.sleep(3)

    # Create a list "price_names" and a list "sorted_product_prices"
    prices = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    price_names = [float(price.text[1::]) for price in prices]
    sorted_product_prices = sorted(price_names)

    assert price_names == sorted_product_prices, 'error'