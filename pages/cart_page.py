from time import sleep
from pages.locators import cart_locators
from pages.base_page import BasePage
from utils.project_ec import text_is_not_empty_in_element
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import common_locators

class CartPage(BasePage):

    def check_empty_cart_page(self):

        empty_cart = self.driver.find_element(*cart_locators.empty_cart_loc)
        assert empty_cart.text == "Your cart is empty!"

        order_overview = self.driver.find_element(*cart_locators.order_overview_loc)
        assert order_overview.is_displayed(), "Блок 'order_overview' не отображается"


    def check_enriched_cart_page(self):
        self.wait.until(EC.element_to_be_clickable(cart_locators.good_image_loc))

        assert self.driver.find_element(*cart_locators.good_image_loc).is_displayed(), "Изображение товара не отображается"
        assert self.driver.find_element(*cart_locators.remove_button_in_cart_loc).is_displayed(), "Кнопка удаления товара из корзины не отображается"

        assert self.driver.find_element(*cart_locators.checkout_button_loc).is_displayed(), "Кнопка 'checkout' не отображается"
        assert self.driver.find_element(*cart_locators.subtotal_area_loc).is_displayed(), "Элемент 'Subtotal' не отображается"
        assert self.driver.find_element(*cart_locators.taxes_area_loc).is_displayed(), "Элемент 'Taxes' не отображается"
        assert self.driver.find_element(*cart_locators.total_area_loc).is_displayed(), "Элемент 'Total' не отображается"
        assert self.driver.find_element(*cart_locators.input_promo_field_loc).is_displayed(), "Поле ввода промокода не отображается"
        assert self.driver.find_element(*cart_locators.apply_promocode_field_loc).is_displayed(), "Кнопка подтверждения промокода не отображается"


    def add_goods_in_cart(self, count: int):
        for _ in range(count):
            self.driver.find_element(*common_locators.add_one_button_loc).click()


    def remove_goods_in_cart(self, count: int):
        for _ in range(count):
            self.driver.find_element(*common_locators.remove_one_button_loc).click()


    def remove_all_goods_in_cart(self):
        """Пока функция удаляет все единицы одного экземпляра товара"""
        try:
            actual_count_in_cart = self.driver.find_element(*cart_locators.count_goods_in_cart_button_loc)
            while actual_count_in_cart.is_displayed():
                self.driver.find_element(*common_locators.remove_one_button_loc).click()
        except:
            pass


    def check_goods_count_in_cart(self, count: int):
        actual_count_in_cart = int(self.driver.find_element(*cart_locators.count_goods_in_cart_button_loc).get_attribute("value"))
        assert count == actual_count_in_cart, f"Ожидалось кол-во товаров {count}, но получено {actual_count_in_cart}"

