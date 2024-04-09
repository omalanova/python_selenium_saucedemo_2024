import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# ТС-205. Подсчет верной общей суммы за заказ
    # 1. Открыть главную страницу сайта
    # 2. Добавить 2 товара (один из 1 тройки, другой из 2 тройки) в Корзину, нажав на кнопку ""Add to cart""
    # 3. Перейти к оформлению заказа
    # 4. Проверить, что отображается верная общая сумма заказа

def test_205(browser, auth):

    # составляю лист из цены и кнопки Add to cart каждого товара, всего 12 элементов в виде объектов
    price_and_addtocart = browser.find_elements(By.CSS_SELECTOR, '.inventory_item_price,.btn_inventory')
    print([i.text for i in price_and_addtocart]) # распечатываю этот лист
    # составляю текстовый лист из цены и кнопки Add to cart каждого товара
    list1 = [i.text for i in price_and_addtocart]

    # определяем рандомные номера товара
    rand_number1 = random.randrange(0,5, 2)
    rand_number2 = random.randrange(6, 11, 2)
    # сумма цен 2х рандомных товаров
    sum_prices_rand = float(list1[rand_number1][1::]) + float(list1[rand_number2][1::])
    print(sum_prices_rand) # распечатываю числовой вид суммы выбранных товаров

    price_and_addtocart[rand_number1 + 1].click() # кликаю на соответств. 1 товару кнопку Add to cart
    price_and_addtocart[rand_number2 + 1].click()  # кликаю на его соответств. 2 товару кнопку Add to cart

    #  переходим в корзину
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(1)
    # находим общую цену товара в корзине
    price_in_cart = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    list2 = [float(i.text[1::]) for i in price_in_cart]
    print(list2)
    price_in_cart_num = sum(list2)
    print(price_in_cart_num) #  распечатываем числовой вид общей цены товаров в корзине

    assert sum_prices_rand == price_in_cart_num
