"""
Author:Bhargav Baleja
CS 555 Agile Methods for Software Development 
Purpose: Testing for user story 33
"""
import unittest, os, io, sys
from Base_Files import Repository, Individual, Family
from US_33 import US_33

class Test_US_33(unittest.TestCase):
    """ Tests US33. checks that list all orphans. """

    def test_US_33(self):
        """ Tests US33. checks that list all orphans. """

        repository = Repository("")
        output = ['@I1@ Mia /Shiyani/ has age 17 and is orphan']
        self.assertEqual(US_33(repository), output)
        self.assertTrue(US_33(repository) == ['@I1@ Mia /Shiyani/ has age 17 and is orphan'])
        self.assertFalse(US_33(repository) == ['@I1@ Yatinkumar /Shiyani/ 13 is orphan and age is less than 18'])
        self.assertTrue(US_33(repository) != ['@I1@ priyanka /Shiyani/ 16 is orphan and age is less than 18'])

if __name__ == "__main__":
    unittest.main(exit=False)
