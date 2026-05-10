from time import sleep
from pages.locators import cart_locators
from pages.base_page import BasePage
from utils.project_ec import text_is_not_empty_in_element

class CartPage(BasePage):

    def check_empty_cart_page(self):

        empty_cart = self.driver.find_element(*cart_locators.empty_cart_loc)
        assert empty_cart.text == "Your cart is empty!"

        order_overview = self.driver.find_element(*cart_locators.order_overview_loc)
        assert order_overview.is_displayed(), "Блок 'order_overview' не отображается"
        sleep(1)


    def check_enriched_cart_page(self):

        self.wait.until(text_is_not_empty_in_element)
        assert self.driver.find_element(*cart_locators.checkout_button_loc).is_displayed(), "Кнопка 'checkout' не отображается"
        assert self.driver.find_element(*cart_locators.good_image_loc).is_displayed(), "Изображение товара не отображается"