import pytest
from selenium import webdriver
from time import sleep


# http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9 (страница какого-то товара)




def test_good_page_displayed(good_page):
    """Проверка отображения страницы товара"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.check_product_page_displayed()

