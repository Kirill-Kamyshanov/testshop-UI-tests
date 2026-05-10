def text_is_not_empty_in_element(locator):

    def _predicate(driver):
        element = driver.find_element(*locator)
        if len(element.text) > 0:
            return True
        else:
            return False

    return _predicate





def text_is_not_empty_in_elements(locator):

    def _predicate(driver):
        elements = driver.find_elements(*locator)
        for element in elements:
            print(element.text)
            if len(element.text) < 0:
                return False
        return True

    return _predicate
