from pages.base_page import BasePage
from pages.locators import good_page_locators

class GoodPage(BasePage):


    def check_product_page_displayed(self):

        price = self.driver.find_element(*good_page_locators.price_area_loc)
        assert price.text.startswith("$") or price.text.startswith("€"), "Цена товара не начинается с '$' или '€'"

        picture = self.driver.find_element(*good_page_locators.good_picture_loc)
        assert picture.is_displayed(), "Картинка товара не отображается"

        add_to_cart_button = self.driver.find_element(*good_page_locators.add_to_cart_from_good_page_loc)
        assert add_to_cart_button.is_displayed(), "Кнопка добавления товара в корзину не отображается на странице товара"

        add_one_button = self.driver.find_element(*good_page_locators.add_one_button_loc)
        assert add_one_button.is_displayed(), "Кнопка увеличения кол-ва товаров не отображается на странице товара"

        remove_one_button = self.driver.find_element(*good_page_locators.remove_one_button_loc)
        assert remove_one_button.is_displayed(), "Кнопка уменьшения кол-ва товаров не отображается на странице товара"

        add_qty_area = self.driver.find_element(*good_page_locators.add_qty_area_loc)
        assert add_qty_area.is_displayed(), "Зона добавления товара не отображается на странице товара"




# /furn-9999-office-design-software-7?category=9