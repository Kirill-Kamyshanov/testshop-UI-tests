from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By




def test_category_page_displayed(category_page):
    """Проверка отображения страницы категории товара"""
    category_page.open_page("/category/desks-1")
    category_page.check_category_page_displayed()



def test_category_page_sort(category_page):
    """Проверка сортировки товаров на странице категории по цене (по возрастанию/по убыванию)"""
    category_page.open_page("/category/desks-1")
    category_page.check_sort()


def test_category_page_search(category_page):
    """Проверка функции поиска товаров на странице категории"""
    category_page.open_page("/category/desks-1")
    category_page.check_search("desk")
