import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.good_page import GoodPage


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


@pytest.fixture
def add_test_good_in_cart(driver, good_page):
    """Фикстура для добавления тестового товара в корзину"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.add_goods_in_card(1)
    return


@pytest.fixture
def good_page(driver):
    return GoodPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def category_page(driver):
    return CategoryPage(driver)
