from time import sleep

from pages.base_page import BasePage
from pages.locators import category_page_locators


class CategoryPage(BasePage):

    def check_category_page_displayed(self):

        product_cards = self.driver.find_elements(*category_page_locators.good_in_category_page_loc)
        assert len(product_cards) > 0, "На странице категории не отображено ни одного товара"

        assert self.driver.find_element(*category_page_locators.filter_by_material_block_loc).is_displayed()

        assert self.driver.find_element(*category_page_locators.search_field_loc).is_displayed()
        assert self.driver.find_element(*category_page_locators.search_button_loc).is_displayed()

        assert self.driver.find_element(*category_page_locators.price_range_text_loc).is_displayed()

        sort_by_title = self.driver.find_element(*category_page_locators.sort_by_text_loc)
        assert sort_by_title.text == "Sort By:", f"Текст не соответствует ожидаемому: {sort_by_title.text}"
        assert self.driver.find_element(*category_page_locators.sort_by_dropdown_field).is_displayed()

        assert self.driver.find_element(*category_page_locators.grid_type_loc).is_displayed()
        assert self.driver.find_element(*category_page_locators.list_type_loc).is_displayed()


    def check_sort(self):

        dd = self.driver.find_element(*category_page_locators.sort_by_dropdown_field)
        dd.click()

        sleep(3)