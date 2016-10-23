import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")


def test_search_in_python_org(self):
    """
    Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
    Note that it does not look for any particular text in search results page. This test verifies that
    the results were not empty.
    """
    pass

if __name__ == "__main__":
    unittest.main()