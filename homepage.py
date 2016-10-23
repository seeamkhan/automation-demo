from base import BasePage
from base import InvalidPageException


class Homepage(BasePage):
    _homepage_slider_id = "viewport"

    def __init__(self, driver):
        super(Homepage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_id(self._homepage_slider_id)
        except:
            raise InvalidPageException("Homepage not loaded")
        