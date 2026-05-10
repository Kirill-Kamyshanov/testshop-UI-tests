

class BasePage:
    host = "http://testshop.qa-practice.com/shop"
    endpoint = None

    def __init__(self, driver):
        self.driver = driver


    def open_page(self, endpoint: str):
        """Открыть страницу"""
        endpoint = endpoint if endpoint.startswith('/') else f'/{endpoint}'
        return self.driver.get(f"{self.host}{endpoint}")