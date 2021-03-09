import unittest

from US23 import *

class UnitTestUS22(unittest.TestCase):
    def setUp(self):
        self.file = "input.ged"
        self.output = US23(self.file)

    def test_us23_1(self):
        self.assertNotIn("US23 : Name Dean /Winchester/ with birthdate AUG_1980 already exists", self.output)
    def test_us23_2(self):
        self.assertIn("US23 : Name Lisa /Braeden/ with birthdate AUG_1980 already exists", self.output) 
    def test_us23_3(self):
        self.assertNotIn("US23 : Name John /Winchester/ with birthdate AUG_1980 already exists", self.output)
    def test_us23_4(self):
        self.assertIn("US23 : Name Adam /Milligan/ with birthdate 29_SEP_1990 already exists", self.output)
    def test_us23_5(self):
        self.assertNotIn("US23 : Name Sam /Winchester/ with birthdate AUG_1980 already exists", self.output)


if __name__ == '__main__':
    unittest.main(verbosity=2)