from basePage import BasePage

class SendBugPage(BasePage):
    _validationText = "Type your team id and bug content:"

    _teamIdEditBox = "/html/body/div/div/form[1]/input"
    _bugDescription = "/html/body/div/div/form[1]/textarea"
    _sendBugButton = "//*[@id='send-button']"

    _team_error_message = "/html/body/div/div/h1"

    def enter_team_id(self, teamid):
        inputbox = self.driver.find_element_by_xpath(self._teamIdEditBox)
        inputbox.clear()
        inputbox.send_keys(teamid)

    def enter_bug_description(self, text):
        inputbox = self.driver.find_element_by_xpath(self._bugDescription)
        inputbox.clear()
        inputbox.send_keys(text)

    def sendBug(self):
        self.driver.find_element_by_xpath(self._sendBugButton).click()

    def getSendingBugStatus(self):
        return self.driver.find_element_by_xpath(self._team_error_message).text


    def _validate_page(self):
        assert self.driver.find_elements_by_link_text(self._validationText)
