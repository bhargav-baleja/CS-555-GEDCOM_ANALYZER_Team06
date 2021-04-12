""" File that contains all the test cases. """
import unittest
from typing import List
import datetime

from Base_Files.Repository import Repository

from User_Stories.US_2 import US_2
from User_Stories.US_3 import US_3
from User_Stories.US_08 import US_08
from User_Stories.US_09 import US_09
from User_Stories.US_11 import US_11
from User_Stories.US_33 import US_33

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

        def test_US_03(self):
            """ Function that tests user story 3 """

            repository = Repository("../GEDCOM_Files/US_03.ged")
            expected = ['US_03: Suresh /Kapoor/ birthday after death date on line number 52',
                        'US_03: Kangana /Patel/ birthday after death date on line number 63']
            actual = US_3(repository.get_individual())
            self.assertEqual(actual, expected)

        def test_US_08(self):
            """ The function is to test US_08 function"""
            repository = Repository('../GEDCOM_Files/US_02.ged')

            expected = [
                "Family id Line number: 523\n The Father @I31@ is younger than his child @I33@ which is illegal."]

            actual = US_08(repository.get_individual(), repository.get_family())

            self.assertEqual(actual, expected)

        def test_us09(self):
            """ The function is to test US_09 function"""
            repository = Repository('../GEDCOM_Files/US_02.ged')

            # The expected output
            expected = ['Family id Line number: 426\n Birth of child @I28@ is before the death of the father @I27@',
                        'Family id Line number: 426\n Birth of child @I28@ is before the death of the mother @I2@',
                        'Family id Line number: 451\n Birth of child @I38@ is before the death of the father @I3@',
                        'Family id Line number: 451\n Birth of child @I38@ is before the death of the mother @I4@',
                        'Family id Line number: 451\n Birth of child @I31@ is before the death of the father @I3@',
                        'Family id Line number: 451\n Birth of child @I31@ is before the death of the mother @I4@',
                        'Family id Line number: 451\n Birth of child @I35@ is before the death of the father @I3@',
                        'Family id Line number: 451\n Birth of child @I35@ is before the death of the mother @I4@']

            actual = US_09(repository.get_individual(), repository.get_family())

            self.assertEqual(actual, expected)

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

        """ Tests US33. checks that list all orphans. """

        def test_US_33(self):
            """ Tests US33. checks that list all orphans. """

            repository = Repository("../GEDCOM_Files/US_33.ged")
            output = ['@I1@ Amrita /Khan/ has age 14 and is orphan']
            self.assertEqual(US_33(repository), output)
            self.assertTrue(US_33(repository) == ['@I1@ Amrita /Khan/ has age 14 and is orphan'])
            self.assertFalse(US_33(repository) == ['@I1@ Saif /Khan/ 13 is orphan and age is less than 18'])
            self.assertTrue(US_33(repository) != ['@I1@ Kareena /Kapoor/ 16 is orphan and age is less than 18'])



if __name__ == "__main__":
    """ Runs all the tests created above. """
    unittest.main(exit=False, verbosity=2)
