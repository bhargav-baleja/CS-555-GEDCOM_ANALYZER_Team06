import unittest

from US27 import *

class UnitTestUS27(unittest.TestCase):

    def setUp(self):
        # self.fam1 = Family("Shaikh")
        # self.dupFam = Family("Shaikh2")
        # self.indi1 = Individual("Irfan01")
        # self.dupIndi1 = Individual("Irfan02")
        self.output = US27()
        

    def test_age_1(self):
        self.assertIn("[US27] Rick /Sanchez/ is 71 years old" ,self.output)
    
    def test_age_2(self):
        self.assertIn("[US27] Mariah /Sanchez/ is 70 years old" ,self.output)

    def test_age_3(self):
        self.assertIn("[US27] Beth /Sanchez/ is 45 years old" ,self.output)
    
    def test_age_4(self):
        self.assertNotIn("[US27] Jerry /Smith/ is 47 years old" ,self.output)
    
    def test_age_5(self):
        self.assertNotIn("[US27] Morty /Smith/ is 26 years old" ,self.output)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)