from selenium.webdriver.chrome.webdriver import WebDriver

class SeleniumWrapper(object):
  _instance = None
  _driverPath = "...\\chromedriver.exe"

  def __new__(cls, base_url):
    if cls._instance is None:
        cls._instance = object.__new__(cls)
        cls.base_url = base_url
        cls.driver = WebDriver(cls._driverPath)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    return cls._instance
