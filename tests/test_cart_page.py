import pytest
import allure


@allure.feature("Cart page")
@pytest.mark.regression
class TestCartPage:
    @pytest.mark.smoke
    def test_empty_cart_displayed(self, cart_page):
        """Проверка отображения элементов в пустой корзине"""
        cart_page.open_page()
        cart_page.check_empty_cart_page()


    @pytest.mark.smoke
    def test_cart_with_a_good(self, good_page, cart_page, add_test_good_in_cart):
        """Проверка наличия товара и отображения веб-элементов в корзине с добавленным товаром"""
        cart_page.open_page()
        cart_page.check_enriched_cart_page()


    @pytest.mark.smoke
    def test_change_goods_count_in_cart(self, good_page, cart_page, add_test_good_in_cart):
        """Проверка изменения количества товара в корзине (увеличение/уменьшение/полная очистка)"""
        cart_page.open_page()
        cart_page.add_goods_in_cart(3)
        cart_page.check_goods_count_in_cart(4)
        cart_page.remove_goods_in_cart(2)
        cart_page.check_goods_count_in_cart(2)
        cart_page.remove_goods_in_cart()
        cart_page.check_empty_cart_page()
