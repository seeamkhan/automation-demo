from base import BasePage
from base import InvalidPageException


class ProductPage(BasePage):

    _product_name_locator = "//h1[contains (@class, 'product-name')]"

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    @property
    def name(self):
        return self.driver.find_element_by_xpath(self._product_name_locator).text().strip()

    @property
    def description(self):
        pass
        # return self.driver.find_element_by_xpath()

    @property
    def price(self):
        pass
        return

    @property
    def size(self):
        pass
        return

    @property
    def color(self):
        pass
        return

    @property
    def quantity(self):
        pass
        return

    @property
    def add_to_cart_button(self):
        pass
        return

    def _validate_page(self, driver):
        pass
        try:
            driver.find_element_by_xpath()
        except:
            raise InvalidPageException("Product page not found!")
