from selenium.webdriver.common.by import By

# товары (плитка)
good_in_category_page_loc = (By.CLASS_NAME, "oe_product")

# Блок фильтр по материалам
filter_by_material_block_loc = (By.ID, "wsale_products_attributes_collapse")

# Бегунок для фильтра по цене
price_range_text_loc = By.XPATH, "//div[@id='o_wsale_price_range_option' and @class='position-relative  ']"

# Блок Search
search_field_loc = (By.CSS_SELECTOR,
                    "[class='search-query form-control oe_search_box border-0 bg-light border-0 text-bg-light']")
search_button_loc = (By.XPATH, "//button[@type='submit' and @class='btn oe_search_button btn btn-light']")

# Блок sort by
sort_by_text_loc = (By.CSS_SELECTOR, '[class="d-none d-lg-inline text-muted"]')
sort_by_dropdown_field = (By.XPATH,
                          '//div[@class="o_sortby_dropdown dropdown dropdown_sorty_by d-none me-auto d-lg-inline-block"]/a[@class="dropdown-toggle btn btn-light"]')
sort_by_price_asc_text = "Price - Low to High"
sort_by_price_desc_text = "Price - High to Low"

# Блок типов отображения
grid_type_loc = (By.CSS_SELECTOR, '[title="Grid"]')
list_type_loc = (By.CSS_SELECTOR, '[title="List"]')
