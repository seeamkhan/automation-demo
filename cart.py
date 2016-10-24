from base import BasePage
from base import InvalidPageException
from product import ProductPage


class CartRegion(BasePage):
    _cart_region_locator = "//a[contains(@class, 'cart-widget-button-container')]"

    def __init__(self, driver):
        super(CartRegion, self).__init__(driver)

    def universal_cart_link(self):
        self.cart_link = self.driver.find_element_by_xpath(self._cart_region_locator)
        return self.cart_link

    def _validate_page(self, driver):
        if self.cart_link not in driver.page_source:
            raise InvalidPageException('Cart link not found!')