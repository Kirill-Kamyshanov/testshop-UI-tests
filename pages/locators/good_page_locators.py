from selenium.webdriver.common.by import By

price_area_loc = (By.CLASS_NAME, 'oe_price')
good_picture_loc = (By.CSS_SELECTOR, '[class="img img-fluid oe_unmovable product_detail_img mh-100"]')
add_to_cart_from_good_page_loc = (By.CSS_SELECTOR, '#add_to_cart')
add_one_button_loc = (By.CSS_SELECTOR, '[title="Add one"]')
remove_one_button_loc = (By.CSS_SELECTOR, '[title="Remove one"]')
add_qty_area_loc = (By.CSS_SELECTOR, '[name="add_qty"]')