from base import BasePage
from base import InvalidPageException
from product import ProductPage


class Homepage(BasePage):
    _homepage_slider_id = "viewport"

    def __init__(self, driver):
        super(Homepage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_id(self._homepage_slider_id)
        except:
            raise InvalidPageException("Homepage not loaded")


class Products(BasePage):
    _product_title_locator_xpath = "//h3[contains (@class, 'product-title')]"
    _product_name_locator_xpath = "//a[contains (@data-hook, 'title')]"
    _product_count = 0
    _products = {}

    def __init__(self, driver):
        super(Products, self).__init__(driver)
        result = self.driver.find_elements_by_xpath(self._product_title_locator_xpath)
        for product in result:
            name = product.driver.find_elements_by_xpath(self._product_name_locator_xpath).text
            # self._products[name] = product.find_element_by_xpath()

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self):
        self._products[product_name].click()
        return ProductPage(self.driver)

