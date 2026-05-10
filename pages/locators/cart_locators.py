from selenium.webdriver.common.by import By

empty_cart_loc = (By.CSS_SELECTOR, '[class="js_cart_lines alert alert-info"]')
order_overview_loc = (By.XPATH, '//h3[text()="Order overview"]')

# Элементы для не пустой корзины
checkout_button_loc = (By.CSS_SELECTOR, '[name="website_sale_main_button"]')
good_image_loc = (By.CSS_SELECTOR, '[class="img o_image_64_max rounded"]')
# прописать разные кнопки которые будут проверяться