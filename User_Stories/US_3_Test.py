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
        
        repository = Repository("")
        output = ['Suresh /Kapoor/ birthday after death date','Kangana /Patel/ birthday after death date']
        self.assertEqual(US_3(repository), output)
        self.assertNotEqual(US_3(repository), ['Ramesh /Patel/ birthday after death date'])
        self.assertTrue(US_3(repository) == ['Suresh /Kapoor/ birthday after death date', 'Kangana /Patel/ birthday after death date'])
        self.assertFalse(US_3(repository) == ['Anushka /Shah/ birthday after death date'])
        self.assertTrue(US_3(repository) != ['Kangana /Patel birthday after death date'])

        
if __name__ == "__main__":
    unittest.main(exit=False)

