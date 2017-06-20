#from selenium.webdriver.chrome.webdriver import WebDriver
from abc import abstractmethod
from seleniumWrapper import SeleniumWrapper

class BasePage(object):
    """ All page objects inherit from this """
    _mainPageUrl = "http://localhost:5002/"
    driver = SeleniumWrapper(_mainPageUrl).driver
    def __init__(self):
        #self._driverPath = "C:\\FP\\szkolenia\\automationBasics\\chromedriver_win32\\chromedriver.exe"
        pass
        #self.driver.get(self._mainPageUrl)

    @abstractmethod
    def _validate_page(self):
        pass

    def verify_if_text_exists(self, text):
        return self.driver.find_element_by_link_text(text)

    """ Regions define functionality available through
        all page objects """
    @property
    def search(self):
        """e.g from search import SearchRegion
        #return SearchRegion(self.driver)"""

    class InvalidPageException(Exception):
        """ Throw this exception when you don't find
        the correct page """
        pass
