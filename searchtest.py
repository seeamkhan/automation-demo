import unittest
from homepage import Homepage
from basetestcase import BaseTestCase


class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = Homepage(self.driver)
        homepage.search.searchFor('earphones')

        # search_result = homepage.search.searchFor('earphones')
        # number_of_product = search_result.product_count
        # print "'%d' product found" %number_of_product
        # self.assertEqual(2, search_result.product_count)



if __name__ == '__main__':
    unittest.main(verbosity=2)
