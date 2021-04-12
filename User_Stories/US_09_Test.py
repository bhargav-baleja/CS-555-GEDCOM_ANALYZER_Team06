"""
Test cases for user story US_09
Author: Bhargav Baleja
"""

import unittest
from User_Stories.US_09 import US_09
from Base_Files.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_09"""

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


if __name__ == "__main__":
    unittest.main(exit=False)