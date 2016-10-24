from abc import abstractmethod


class BasePage(object):
    """All page objects inherit from this."""
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return


    """Region define functionalities through all page objects"""
    @property
    def cart(self):
        from cartpage import CartRegion
        return CartRegion(self.driver)

class InvalidPageException(Exception):
    """Throw this exception when you dont find the correct page."""
    pass
