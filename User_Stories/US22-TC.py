import unittest

from US22 import *

class UnitTestUS22(unittest.TestCase):

    def setUp(self):
        self.fam1 = Family("Shaikh")
        self.dupFam = Family("Shaikh2")
        self.indi1 = Individual("Irfan01")
        self.dupIndi1 = Individual("Irfan02")
        

    def test_indi_insert(self):
        self.assertTrue(saveIndi(self.indi1))
    
    def test_fam_insert(self):
        self.assertTrue(saveFam(self.fam1))
    
    def test_duplicate_indi_insert(self):
        saveIndi(self.dupIndi1)
        self.assertFalse(saveIndi(self.dupIndi1))
    
    def test_duplicate_fam_insert(self):
        saveFam(self.dupFam)
        self.assertFalse(saveFam(self.dupFam))

    def test_instance_of_indi(self):
        self.assertTrue(isinstance(self.indi1,Individual))

    def test_instance_of_indi(self):
        self.assertTrue(isinstance(self.indi1,Individual))

if __name__ == '__main__':
    unittest.main(verbosity=2)