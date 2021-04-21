"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 06
"""


import unittest
from US_06 import US_06
from Base_Files.Repository import Repository


class Test(unittest.TestCase):

    def test_US_06(self):
        """ Contains test cases for US_06"""
        repository = Repository("../GEDCOM_Files/US_06.ged")

        actual = ['US_06: Saumya /Shah/ Death 1822-01-03 occured prior to the divorce date 1852-07-14']

        output = US_06(repository.get_individual(), repository.get_family())

        self.assertEqual(output, actual)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=1)