import unittest
import time
from homepage import Homepage
from basetestcase import BaseTestCase
from search import SearchResults


class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = Homepage(self.driver)
        # homepage.search.searchFor('earphones')


        search_result = homepage.search.searchFor('earphones')
        number_of_product = search_result.product_count
        # number_of_product = SearchResults(self.driver).product_count
        # number_of_product = searchresults.product_count
        print "Total number of products in the page: %d" %number_of_product
        # self.assertEqual(2, search_result.product_count)
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
