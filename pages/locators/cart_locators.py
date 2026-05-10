from selenium.webdriver.common.by import By

empty_cart_loc = (By.CSS_SELECTOR, '[class="js_cart_lines alert alert-info"]')
order_overview_loc = (By.XPATH, '//h3[text()="Order overview"]')