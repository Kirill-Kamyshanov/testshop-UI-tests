import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.good_page import GoodPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture
def good_page(driver):
    return GoodPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def category_page(driver):
    return CategoryPage(driver)