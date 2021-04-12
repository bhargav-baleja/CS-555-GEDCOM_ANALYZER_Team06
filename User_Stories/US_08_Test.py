"""
Test cases for user story US_08
Author: Bhargav Baleja
"""

import unittest
from User_Stories.US_08 import US_08
from Base_Files.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_08"""

    def test_US_08(self):
        """ The function is to test US_08 function"""
        repository = Repository('../GEDCOM_Files/US_02.ged')

        # The expected output
        expected = ["Family id Line number: 523\n The Father @I31@ is younger than his child @I33@ which is illegal."]

        # generating a list of the output from the function
        actual = US_08(repository.get_individual(), repository.get_family())

        self.assertEqual(actual, expected)  # positive test result

if __name__ == "__main__":
    unittest.main(exit=False)