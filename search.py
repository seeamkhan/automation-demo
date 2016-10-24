from base import BasePage
from base import InvalidPageException
from product import ProductPage


class SearchRegion(BasePage):
    _search_box_locator = 'field-keywords'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver.find_element_by_name(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)


class SearchResults(BasePage):
    _product_link_locator = "//li[contains (@id, 'result_1')]//a[contains (@class, 's-access-detail-page')]"
    all_product_list = []

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver.find_elements_by_xpath(self._product_link_locator)
        for element in results:
            # print i.get_attribute("href")
            self.all_product_list.append(element.get_attribute("href"))
        driver.get(self.all_product_list[0])
        # return ProductPage(self.driver)

    @property
    def product_count(self):
        return len(self.all_product_list)

    def get_products(self, number):
        return self.all_product_list[number]

