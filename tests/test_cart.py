import pytest
import selenium
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = selenium.webdriver.Chrome()
    driver.maximize_window()
    return driver

# 1 http://testshop.qa-practice.com/shop/cart (корзина)
# 2 http://testshop.qa-practice.com/shop/category/desks-1 (товары категории)
# 3 http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9 (страница какого-то товара)

empty_cart_loc = (By.CSS_SELECTOR, '[class="js_cart_lines alert alert-info"]')

def test_empty_cart(driver):
    """Проверка отображения элементов в пустой корзине"""
    driver.get("http://testshop.qa-practice.com/shop/cart")
    empty_cart = driver.find_element(*empty_cart_loc)
    assert empty_cart.text == "Your cart is empty!" # позже убрать хардкод
    sleep(3)