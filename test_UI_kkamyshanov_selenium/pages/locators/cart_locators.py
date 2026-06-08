from selenium.webdriver.common.by import By

order_overview_loc = (By.XPATH, '//h3[text()="Order overview"]')

# элементы для пустой корзины
empty_cart_loc = (By.CSS_SELECTOR, '[class="js_cart_lines alert alert-info"]')

# Элементы для не пустой корзины
checkout_button_loc = (By.CSS_SELECTOR, '[name="website_sale_main_button"]')
good_image_loc = (By.CSS_SELECTOR, '[class="img o_image_64_max rounded"]')
remove_button_in_cart_loc = (By.XPATH, '//a[text()="Remove"]')

subtotal_area_loc = (By.ID, "cart_total_subtotal")
taxes_area_loc = (By.ID, "order_total_taxes")
total_area_loc = (By.ID, "order_total")

input_promo_field_loc = (By.CSS_SELECTOR, '[name="promo"]')
apply_promocode_field_loc = (By.XPATH, '//a[@role="button" and text()="Apply"]')

count_goods_in_cart_button_loc = (By.XPATH, '//input[@data-product-id="7"]')
