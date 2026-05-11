from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    host = "http://testshop.qa-practice.com/shop"
    endpoint = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 12)

    def open_page(self, endpoint: str = None):
        """Открыть страницу"""
        endpoint = self.endpoint if not endpoint else endpoint
        endpoint = endpoint if endpoint.startswith('/') else f'/{endpoint}'
        return self.driver.get(f"{self.host}{endpoint}")

    def find(self, locator: tuple):
        """Найти один элемент по локатору"""

        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        """Найти несколько элементов по локатору"""

        return self.driver.find_elements(*locator)
