"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 05
"""

import unittest
from User_Stories.US_05 import US_05
from Base_Files.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_05"""

    def test_us05(self):
        """ The function is to test US_05 function"""
        repository = Repository('../GEDCOM_Files/US_02.ged')

        actual = ['Marriage date Line: 447\nDeath of wife date Line: 61\nThe family @F3@ has a death of wife @I4@ before the marriage date.', 'Marriage date Line: 545\nDeath of Husband date Line: 400\nThe family @F18@ has a death of husband @I38@ before the marriage date.']

        output = US_05(repository.get_individual(), repository.get_family())

        self.assertEqual(output, actual)

if __name__ == "__main__":
    unittest.main(exit=False)