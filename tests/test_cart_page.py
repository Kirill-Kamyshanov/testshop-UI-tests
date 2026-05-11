import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By




# 1 http://testshop.qa-practice.com/shop/cart (корзина)
# 2 http://testshop.qa-practice.com/shop/category/desks-1 (товары категории)
# 3 http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9 (страница какого-то товара)



# написать два теста

def test_empty_cart_displayed(cart_page):
    """Проверка отображения элементов в пустой корзине"""
    cart_page.open_page("/cart")
    cart_page.check_empty_cart_page()




def test_cart_with_a_good(good_page, cart_page):
    """Проверка отображения элементов в обогащённой корзине после добавления товара"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.add_goods_in_card(1)
    cart_page.open_page("/cart")
    cart_page.check_enriched_cart_page()




def test_change_goods_count_in_cart(good_page, cart_page):
    """Проверка изменения количества товара в корзине (увеличение/уменьшение/полная очистка)"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.add_goods_in_card(1)
    cart_page.open_page("/cart")
    cart_page.add_goods_in_cart(3)
    cart_page.check_goods_count_in_cart(4)
    cart_page.remove_goods_in_cart(2)
    cart_page.check_goods_count_in_cart(2)
    cart_page.remove_all_goods_in_cart()
    cart_page.check_empty_cart_page()

