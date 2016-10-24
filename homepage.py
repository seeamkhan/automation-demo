from base import BasePage
from base import InvalidPageException
from product import ProductPage


class Homepage(BasePage):
    _homepage_critical_content_xpath = "//div[contains(@class, 'gw-critical-content')]"
    opt_out_id = "redir-opt-out"
    stay_current_site_id = "redir-stay-at-www"

    def __init__(self, driver):
        super(Homepage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_id(self._homepage_critical_content_xpath)
        except:
            raise InvalidPageException("Homepage not loaded")

        try:
            driver.find_element_by_id(self.opt_out_id).click()
            driver.find_element_by_id(self.stay_current_site_id).click()
        except:
            pass