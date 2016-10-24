from base import BasePage
from base import InvalidPageException


class ProductPage(BasePage):
    # _product_name_locator = "//h1[contains (@class, 'product-name')]"
    _buy_box_id_element = "buybox_feature_div"
    _add_to_cart_button_id_element = "add-to-cart-button"
    _proceed_to_checkout_1_element = "//a[contains (text(), 'Proceed to checkout (1 item)')]"
    _cart_link_id_element = "hlb-view-cart-announce"
    _product_title_in_cart_element = "//span[contains (@class, 'a-size-medium sc-product-title')]"

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def buy_box(self):
        assert self.driver.find_element_by_id(self._buy_box_id_element)

    def add_product(self):
        self.driver.find_element_by_id(self._add_to_cart_button_id_element).click()

    def checkout_link(self):
        assert self.driver.find_element_by_xpath(self._proceed_to_checkout_1_element)

    def add_to_cart_button(self):
        assert self.driver.find_element_by_id(self._cart_link_id_element)

    def goto_cart(self):
        self.driver.find_element_by_id(self._cart_link_id_element).click()
        prod_title = self.driver.find_element_by_xpath(self._product_title_in_cart_element).text
        print "'%s' has been Successfully added in your cart!" % prod_title
    # @property
    # def name(self):
    #     return self.driver.find_element_by_xpath(self._product_name_locator).text().strip()





    # @property
    # def description(self):
    #     pass
    #     # return self.driver.find_element_by_xpath()
    #
    # @property
    # def price(self):
    #     pass
    #     return
    #
    # @property
    # def size(self):
    #     pass
    #     return
    #
    # @property
    # def color(self):
    #     pass
    #     return
    #
    # @property
    # def quantity(self):
    #     pass
    #     return


    def _validate_page(self, driver):
        pass
        try:
            driver.find_element_by_xpath()
        except:
            raise InvalidPageException("Product page not found!")
