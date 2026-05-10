from time import sleep

from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.locators import good_page_locators
from pages.locators.common_locators import count_goods_in_card


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



    def check_add_in_card(self, count: int):
        if not isinstance(count, int):
            raise TypeError("Ожидается числовой тип данных")
        if count < 0:
            raise ValueError("Ожидается число больше нуля")


        while count > 1:
            self.driver.find_element(*good_page_locators.add_one_button_loc).click()
            count-= 1


        add_button = self.driver.find_element(*good_page_locators.add_to_cart_from_good_page_loc)
        add_button.click()

        cart_icon = self.driver.find_element(*count_goods_in_card) # товар добавляется, но не находится этот элемент (корзина с числом)
        print(cart_icon.text)

        # count_goods_in_card = (By.XPATH,
        #                        '//sup[@class="my_cart_quantity badge text-bg-primary position-absolute top-0 end-0 mt-n1 me-n1 rounded-pill "]')

        sleep(2)
        # elem = self.driver.find_element(*count_goods_in_card)
        # print(elem.text)

        # price_area_loc = (By.CLASS_NAME, 'oe_price')
        # good_picture_loc = (By.CSS_SELECTOR, '[class="img img-fluid oe_unmovable product_detail_img mh-100"]')
        # add_to_cart_from_good_page_loc = (By.CSS_SELECTOR, '#add_to_cart')
        # add_one_button_loc = (By.CSS_SELECTOR, '[title="Add one"]')
        # remove_one_button_loc = (By.CSS_SELECTOR, '[title="Remove one"]')
        # add_qty_area_loc = (By.CSS_SELECTOR, '[name="add_qty"]')