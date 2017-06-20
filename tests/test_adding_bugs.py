# -*- coding: utf-8 -*-
import unittest
from baseTestCase import BaseTestCase
from pages.mainPage import MainPage


class AddingBugInSystemTest(BaseTestCase):

    def testUnauthorizedTeamCouldNotAddBug(self):
        sendBugPage = MainPage().sendBug()
        sendBugPage.enter_team_id("123")
        sendBugPage.enter_bug_description("testBug")
        sendBugPage.sendBug()

        assert sendBugPage.getSendingBugStatus() == u"Team with id: '123' was not found."

if __name__ == '__main__':
    unittest.main()