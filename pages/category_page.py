from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import category_page_locators
from utils import project_ec


class CategoryPage(BasePage):

    def check_category_page_displayed(self):
        """Проверка отображения страницы категории товара"""

        product_cards = self.find_all(category_page_locators.good_in_category_page_loc)
        assert len(product_cards) > 0, "На странице категории не отображено ни одного товара"

        assert self.find(category_page_locators.filter_by_material_block_loc).is_displayed()

        assert self.find(category_page_locators.search_field_loc).is_displayed()
        assert self.find(category_page_locators.search_button_loc).is_displayed()

        assert self.find(category_page_locators.price_range_text_loc).is_displayed()

        sort_by_title = self.find(category_page_locators.sort_by_text_loc)
        assert sort_by_title.text == "Sort By:", f"Текст не соответствует ожидаемому: {sort_by_title.text}"
        assert self.find(category_page_locators.sort_by_dropdown_field).is_displayed()

        assert self.find(category_page_locators.grid_type_loc).is_displayed()
        assert self.find(category_page_locators.list_type_loc).is_displayed()

    def check_sort_by_price(self):
        """Сортировка товаров по цене(ASC/DESC)"""

        texts = [category_page_locators.sort_by_price_asc_text, category_page_locators.sort_by_price_desc_text]

        for text in texts:
            self.driver.find_element(*category_page_locators.sort_by_dropdown_field).click()
            option = self.find((By.XPATH, f'//*[contains(text(), "{text}")]'))

            self.wait.until(project_ec.text_is_not_empty_in_element((By.XPATH, f'//*[contains(text(), "{text}")]')))
            option.click()

            product_cards = self.find_all(category_page_locators.good_in_category_page_loc)

            sequence_before = [int(card.text[card.text.index("$") + 2:-3].replace(',', '')) for card in product_cards]
            reverse = True if text == "Price - High to Low" else False
            sequence_after = sorted(sequence_before, reverse=reverse)

            assert sequence_before == sequence_after, "Сортировка прошла некорректно"

    def search_by_keyword(self, search_word: str):
        """Поиск товаров по ключевому слову"""

        search_field = self.find(category_page_locators.search_field_loc)
        search_field.send_keys(search_word)
        self.find(category_page_locators.search_button_loc).click()

    def check_searching_results(self, search_word: str):
        """Проверка результатов поиска товаров по ключевому слову"""

        # ждём пока подгрузятся изменения
        initial_count = len(self.find_all(category_page_locators.good_in_category_page_loc))
        self.wait.until(
            lambda d: len(d.find_elements(*category_page_locators.good_in_category_page_loc)) != initial_count)

        # проверка
        product_cards = self.find_all(category_page_locators.good_in_category_page_loc)
        for product_card in product_cards:
            assert search_word in product_card.text.lower(), f"Элемент не содержит слово-фильтр: {product_card.text.lower()}"
