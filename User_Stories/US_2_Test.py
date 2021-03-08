"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 02
"""

import unittest
from Base_Files.Repository import Repository
from User_Stories.US_2 import US_2

class Test_US_02(unittest.TestCase):
    """ Function that tests user story 2 """

    def test_US_02(self):
        """ FUnction that tests user story 2 """
        repository = Repository("../GEDCOM_Files/US_02.ged")
        expected = ['US_02: Bholu /Desai/ birthday after marriage date on line number 439',
                    'US_02: Naina /Shah/ birthday after marriage date on line number 528',
                    'US_02: Mayur /Desai/ birthday after marriage date on line number 528',
                    'US_02: Keval /Kuchadiya/ birthday after marriage date on line number 545']
        actual = US_2(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main(exit=False)