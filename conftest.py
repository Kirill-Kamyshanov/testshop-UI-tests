from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.good_page import GoodPage
from selenium.webdriver.support import expected_conditions as EC

from pages.locators.cart_locators import checkout_button_loc


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


@pytest.fixture
def add_test_good_in_cart(driver, good_page):
    """Фикстура для добавления тестового товара в корзину"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.add_goods_in_card(1)
    # sleep(1)
    yield



@pytest.fixture
def good_page(driver):
    return GoodPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def category_page(driver):
    return CategoryPage(driver)