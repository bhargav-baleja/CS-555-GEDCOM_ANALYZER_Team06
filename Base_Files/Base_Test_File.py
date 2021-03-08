""" File that contains all the test cases. """
import unittest
from typing import List
import datetime

from Base_Files.Repository import Repository

class TestRepository(unittest.TestCase):
    """ Class that contains all the test cases. """

    def __init__(self, *args, **kwargs):
        """ Function that initializes class variable repository. """
        super(TestRepository, self).__init__(*args, **kwargs)
        # Creating an object of class Repository that will contains both individual and family dictionaries.
        # Pass the path of your GEDCOM file as a parameter below.
        self.repository = Repository('../GedcomFiles/')

if __name__ == "__main__":
    """ Runs all the tests created above. """
    unittest.main(exit=False, verbosity=2)
