from time import sleep
from typing import Literal

from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.locators import good_page_locators
from pages.locators.common_locators import count_goods_in_card, change_currency_button, change_to_eur_button
from utils.project_ec import text_is_not_empty_in_element

class GoodPage(BasePage):


    def check_product_page_displayed(self):

        price = self.driver.find_element(*good_page_locators.price_area_loc)
        assert price.text.startswith("$") or price.text.endswith("€"), "Цена товара не отображается в '$' или '€'"

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



    def add_goods_in_card(self, count: int):
        if not isinstance(count, int):
            raise TypeError("Ожидается числовой тип данных")
        if count < 0:
            raise ValueError("Ожидается число больше нуля")


        while count > 1:
            self.driver.find_element(*good_page_locators.add_one_button_loc).click()
            count-= 1


        add_button = self.driver.find_element(*good_page_locators.add_to_cart_from_good_page_loc)
        add_button.click()
        self.wait.until(text_is_not_empty_in_element(count_goods_in_card))


    def assert_goods_was_added_in_card(self, expected_count: int):
        self.wait.until(text_is_not_empty_in_element(count_goods_in_card))

        popup_text = self.driver.find_element(*good_page_locators.popup_title)
        assert popup_text.is_displayed(), "Попап с сообщением о добавлении товара не отобразился"

        cart_icon = self.driver.find_element(*count_goods_in_card)

        assert int(cart_icon.text) == expected_count, (
            f"Неправильное значение кол-ва товаров у иконки корзины: {cart_icon.text}, ожидалось {expected_count}"
        )

    def change_currency_to_EUR(self):
        self.driver.find_element(*change_currency_button).click()
        self.wait.until(text_is_not_empty_in_element(change_to_eur_button))
        self.driver.find_element(*change_to_eur_button).click()


    def assert_price_displayed_in_currency(self, currency_sign: Literal["$", "€"]):
        """Здесь поведение системы специфическое: если цена товара в долларах, знак ставится в начале, если в евро -
        в конце. В реальном проекте уточнил зачем так сделано, а тут просто подстроился"""

        allowed = ["$", "€"]
        if currency_sign not in allowed:
            raise ValueError(f"Некорректная валюта. Допустимые: {allowed}")

        price = self.driver.find_element(*good_page_locators.price_area_loc)

        if currency_sign == "$":
            assert price.text.startswith(f"{currency_sign}"), f"Цена товара не в валюте'{currency_sign}'"
        elif currency_sign == "€":
            assert price.text.endswith(f"{currency_sign}"), f"Цена товара не в валюте'{currency_sign}'"



        # count_goods_in_card = (By.XPATH,
        #                        '//sup[@class="my_cart_quantity badge text-bg-primary position-absolute top-0 end-0 mt-n1 me-n1 rounded-pill "]')

        # sleep(2)
        # elem = self.driver.find_element(*count_goods_in_card)
        # print(elem.text)

        # price_area_loc = (By.CLASS_NAME, 'oe_price')
        # good_picture_loc = (By.CSS_SELECTOR, '[class="img img-fluid oe_unmovable product_detail_img mh-100"]')
        # add_to_cart_from_good_page_loc = (By.CSS_SELECTOR, '#add_to_cart')
        # add_one_button_loc = (By.CSS_SELECTOR, '[title="Add one"]')
        # remove_one_button_loc = (By.CSS_SELECTOR, '[title="Remove one"]')
        # add_qty_area_loc = (By.CSS_SELECTOR, '[name="add_qty"]')