# -*- coding: utf-8 -*-
import unittest
from baseTestCase import BaseTestCase
from pages.mainPage import MainPage


class AddingBugInSystemTest(BaseTestCase):

    def testUnauthorizedTeamCouldNotAddBug(self):
        sendBugPage = MainPage().sendBug()
        #toDo

        assert sendBugPage.getSendingBugStatus() == #ToDO

if __name__ == '__main__':
    unittest.main()