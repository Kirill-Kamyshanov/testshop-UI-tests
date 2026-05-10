import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By




# 1 http://testshop.qa-practice.com/shop/cart (корзина)
# 2 http://testshop.qa-practice.com/shop/category/desks-1 (товары категории)
# 3 http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9 (страница какого-то товара)





def test_empty_cart_displayed(cart_page):
    """Проверка отображения элементов в пустой корзине"""
    cart_page.open_page("/cart")
    cart_page.check_empty_cart_page()




@pytest.mark.skip
def test_cart_with_a_good(driver):
    """Проверка отображения элементов в корзине после добавления товара"""