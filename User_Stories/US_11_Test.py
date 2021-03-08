"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development 
Purpose: Testing for user story 11
"""
import unittest
from Base_Files.Repository import Repository
from User_Stories.US_11 import US_11

class Test_US11(unittest.TestCase):
    """ Tests that husbands and wifes are not married twice at the same time. """

    def test_user_story_11(self):
        """ Tests that husbands and wifes are not married twice at the same time and prints out the cases if so"""
        repository = Repository('../GEDCOM_Files/US_11.ged')
        output = ['Ramesh /Patel/married twice at the same time', 'Anushka /Shah/married twice at the same time']
        self.assertEqual(US_11(repository), output)
        self.assertNotEqual(US_11(repository), ['Suresh /Kapoor married twice on the same time'])
        self.assertTrue(US_11(repository) == ['Ramesh /Patel/married twice at the same time', 'Anushka /Shah/married twice at the same time'])
        self.assertFalse(US_11(repository) == ['Kangana /Patel married twice on the same time'])
        self.assertTrue(US_11(repository) != ['Suresh /Patel married twice on the same time'])


if __name__ == "__main__":
    unittest.main(exit=False)

