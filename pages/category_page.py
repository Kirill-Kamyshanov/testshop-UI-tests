from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import category_page_locators
from utils import project_ec

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
        texts = [category_page_locators.sort_by_price_asc_text, category_page_locators.sort_by_price_desc_text]

        for text in texts:
            self.driver.find_element(*category_page_locators.sort_by_dropdown_field).click()

            # option = self.driver.find_element(By.XPATH, '//*[contains(text(), "Price - Low to High")]')
            option = self.driver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')
            # option = self.driver.find_element(By.XPATH, '//*[contains(text(), "Name (A-Z)")]')

            self.wait.until(project_ec.text_is_not_empty_in_element((By.XPATH, f'//*[contains(text(), "{text}")]')))
            option.click()

            product_cards = self.driver.find_elements(*category_page_locators.good_in_category_page_loc)

            sequence_before = [int(card.text[card.text.index("$") + 2:-3].replace(',', '')) for card in product_cards]

            reverse = True if text == "Price - High to Low" else False
            sequence_after = sorted(sequence_before, reverse=reverse)
            assert sequence_before == sequence_after, "Сортировка прошла некорректно"




