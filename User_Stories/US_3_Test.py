"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development 
Purpose: Testing for user story 03
"""
import unittest
from Base_Files.Repository import Repository
from User_Stories.US_3 import US_3

class Test_US03(unittest.TestCase):
    
    def test_US_03(self):
        """ Function that tests user story 3 """
        
        repository = Repository("../GEDCOM_Files/US_03.ged")
        expected = ['US_03: Suresh /Kapoor/ birthday after death date on line number 52','US_03: Kangana /Patel/ birthday after death date on line number 63']
        actual = US_3(repository.get_individual())
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(exit=False)

