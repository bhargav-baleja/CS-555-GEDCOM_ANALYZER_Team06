import unittest

from US19 import *

class UnitTestUS19(unittest.TestCase):

    def setUp(self):
        # self.fam1 = Family("Shaikh")
        # self.dupFam = Family("Shaikh2")
        # self.indi1 = Individual("Irfan01")
        # self.dupIndi1 = Individual("Irfan02")
        self.output = US19()
        

    def test_cousin_marriage_1(self):
        self.assertIn("[US19] Cousins cannot marry each other :: Morty /Smith/ to Brenda /Rockefeller/" ,self.output)
    
    def test_cousin_marriage_2(self):
        self.assertNotIn("[US19] Cousins cannot marry each other :: Rick /Sanchez/ to Mariah /Sanchez/" ,self.output)
    
    def test_cousin_marriage_3(self):
        self.assertNotIn("[US19] Cousins cannot marry each other :: Beth /Sanchez/ to Jerry /Smith/" ,self.output)
    
    def test_cousin_marriage_4(self):
        self.assertNotIn("[US19] Cousins cannot marry each other :: Dave /Rockefeller/ to Marry /Sanchez/" ,self.output)
    
    def test_family_tree_dict(self):
        self.assertTrue(FAMILY_TREE)


if __name__ == '__main__':
    unittest.main(verbosity=2)