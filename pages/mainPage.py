from basePage import BasePage
from sendBugPage import SendBugPage


class MainPage(BasePage):
    _sendBugButton = "//div[@class='container']//button[.='Send bug']"

    def __init__(self):
        self.driver.get(self._mainPageUrl)

    def sendBug(self):
        self.driver.find_element_by_xpath(self._sendBugButton).click()
        return SendBugPage()

    def _validate_page(self):
        pass
