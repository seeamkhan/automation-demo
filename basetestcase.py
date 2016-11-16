import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # create a new chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Navigate to homepage
        base_url = 'https://www.amazon.com/'
        self.driver.get(base_url)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()
