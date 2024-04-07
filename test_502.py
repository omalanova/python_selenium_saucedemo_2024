from selenium.webdriver.common.by import By

# ТС-502. Проверка работоспособности фильтра (Z to A)
    # 1. Открыть главную страницу
    # 2. Перейти в каталог товаров из меню навигации
    # 3. В выпадающем списке выбрать фильтр Z-A
    # 4. Убедиться, что товары отсортированы в обратном алфавитном порядке

def test_502(browser, auth):

    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()
    from selenium.webdriver.support.select import Select
    select = Select(dropdown)
    select.select_by_index(1)
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_label')
    product_names = [product.text for product in products]
    sorted_product_names = sorted(product_names, reverse=True)
    assert product_names == sorted_product_names, 'что-то не то'