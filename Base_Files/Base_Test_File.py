""" File that contains all the test cases. """
import unittest
from typing import List
import datetime

from Base_Files.Repository import Repository

from User_Stories.US_2 import US_2
from User_Stories.US_11 import US_11

class TestRepository(unittest.TestCase):
    """ Class that contains all the test cases. """

    def __init__(self, *args, **kwargs):
        """ Function that initializes class variable repository. """
        super(TestRepository, self).__init__(*args, **kwargs)
        # Creating an object of class Repository that will contains both individual and family dictionaries.
        # Pass the path of your GEDCOM file as a parameter below.

        """ Function that tests user story 2 """
        def test_US_02(self):
            """ Function that tests user story 2 """
            repository = Repository("../GEDCOM_Files/US_02.ged")
            expected = ['US_02: Bholu /Desai/ birthday after marriage date on line number 439',
                        'US_02: Naina /Shah/ birthday after marriage date on line number 528',
                        'US_02: Mayur /Desai/ birthday after marriage date on line number 528',
                        'US_02: Keval /Kuchadiya/ birthday after marriage date on line number 545']
            actual = US_2(repository.get_individual(), repository.get_family())
            self.assertEqual(expected, actual)

        """ Tests that husbands and wifes are not married twice at the same time. """

        def test_user_story_11(self):
            """ Tests that husbands and wifes are not married twice at the same time and prints out the cases if so"""

            repository = Repository('../GEDCOM_Files/US_11.ged')
            output = ['Ramesh /Patel/married twice at the same time', 'Anushka /Shah/married twice at the same time']
            self.assertEqual(US_11(repository), output)
            self.assertNotEqual(US_11(repository), ['Suresh /Kapoor married twice on the same time'])
            self.assertTrue(US_11(repository) == ['Ramesh /Patel/married twice at the same time',
                                                  'Anushka /Shah/married twice at the same time'])
            self.assertFalse(US_11(repository) == ['Kangana /Patel married twice on the same time'])
            self.assertTrue(US_11(repository) != ['Suresh /Patel married twice on the same time'])

if __name__ == "__main__":
    """ Runs all the tests created above. """
    unittest.main(exit=False, verbosity=2)
