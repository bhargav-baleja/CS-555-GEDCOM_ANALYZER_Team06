import unittest

from US30 import *

class UnitTestUS30(unittest.TestCase):
    def setUp(self):
        self.file = "../GEDCOM_Files/US_29-30.ged"
        self.output = US30(self.file)

    def test_us30_1(self):
        self.assertIn("[US30] @I2@ is alive and married", self.output)
    def test_us30_2(self):
        self.assertNotIn("[US30] @I5@ is alive and married", self.output) 
    def test_us30_3(self):
        self.assertNotIn("[US30] @I6@ is alive and married", self.output)
    def test_us30_4(self):
        self.assertIn("[US30] @I4@ is alive and married", self.output)
    def test_us30_5(self):
        self.assertIn("[US30] @I3@ is alive and married", self.output)

if __name__ == '__main__':
    unittest.main(verbosity=2)