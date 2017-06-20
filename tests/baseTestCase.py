import unittest
from basePage import BasePage


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self._basePage = BasePage()

    def tearDown(self):
        # close the browser window
        self._basePage.driver.quit()
