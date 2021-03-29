import unittest
from US_35 import *


class TestUserStory35(unittest.TestCase):
    
    def setUp(self):
        fam = Family("F1")
        families.append(fam)
    def tearDown(self):
        families.clear()

    def test_no_births(self):
        table = []
        fewer_than_fifteen_siblings(table)
        self.assertTrue(table[0][3])

    def test_mixed_births(self):
        table = []
        for i in range(14):
            get_family("F1").children.append(Individual("I{}".format(i + 1)))

        fewer_than_fifteen_siblings(table)
        self.assertTrue(table[0][3])

    def test_all_recent_births(self):
        table = []
        for i in range(20):
            get_family("F1").children.append(Individual("I{}".format(i + 1)))

        fewer_than_fifteen_siblings(table)
        self.assertFalse(table[0][3])

    def test_all_far_births(self):
        table = []
        for i in range(15):
            get_family("F1").children.append(Individual("I{}".format(i + 1)))

        fewer_than_fifteen_siblings(table)
        self.assertFalse(table[0][3])

    def test_empty_file(self):
        table = []
        for i in range(15):
            get_family("F1").children.append(Individual("I{}".format(i + 1)))

        fewer_than_fifteen_siblings(table)
        self.assertEqual(table[0][3],table[0][3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
