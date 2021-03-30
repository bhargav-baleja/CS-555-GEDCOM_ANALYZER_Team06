import unittest

from US29 import *

class UnitTestUS29(unittest.TestCase):
    def setUp(self):
        self.file = "../GEDCOM_Files/US_29-30.ged"
        self.output = US29(self.file)

    def test_us29_1(self):
        self.assertIn("[US29] @I5@ is deceased", self.output)
    def test_us29_2(self):
        self.assertNotIn("[US29] @I4@ is deceased", self.output) 
    def test_us29_3(self):
        self.assertNotIn("[US29] @I3@ is deceased", self.output)
    def test_us29_4(self):
        self.assertIn("[US29] @I8@ is deceased", self.output)
    def test_us29_5(self):
        self.assertIn("[US29] @I6@ is deceased", self.output)

if __name__ == '__main__':
    unittest.main(verbosity=2)