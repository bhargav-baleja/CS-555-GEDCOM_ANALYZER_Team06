"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 02
"""

import unittest
from Base_Files.Repository import Repository
from User_Stories.US_02 import US_02

class Test_US_02(unittest.TestCase):
    """ Function that tests user story 3 """
    def test_US_02(self):
        """ FUnction that tests user story 2 """
        repository = Repository("../GedcomFiles/US_02.ged")
        expected = ['US_02: Micheal /Mia/ birthday after marriage date on line number 604',
                    'US_02: Mike /Robinson/ birthday after marriage date on line number 604',
                    'US_02: Sam /Robinson/ birthday after marriage date on line number 633']
        actual = US_02(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)