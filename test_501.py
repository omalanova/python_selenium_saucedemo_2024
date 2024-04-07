import time

from selenium.webdriver.common.by import By

# ТС-501. Проверка работоспособности фильтра (A to Z)
    # 1. Открыть главную страницу
    # 2. Перейти в каталог товаров из меню навигации
    # 3. В выпадающем списке выбрать фильтр A-Z
    # 4. Убедиться, что товары отсортированы в алфавитном порядке

def test_501(browser, auth):

    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()
    from selenium.webdriver.support.select import Select
    select = Select(dropdown)
    select.select_by_index(0)
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_label')
    product_names = [product.text for product in products]
    sorted_product_names = sorted(product_names)
    assert product_names == sorted_product_names, 'что-то не то'