import unittest
from User_Stories.US_12 import US_12
from Base_Files.Repository import Repository

class Test(unittest.TestCase):

    def test_US_12(self):
        """ Contains test cases for US_12"""
        indi_repo: Repository = Repository("../GEDCOM_Files/US_12.ged")

        exp = ["US_12: Yatinkumar /Shiyani/ with @I27@ is 80 years or older than Mia /Shiyani/ id:{'@I28@'} in line number 398 ", "US_12: Priyanka /Robinson/ with @I2@ is 60 years or older than Mia /Shiyani/ id:{'@I28@'} in line number 398 "]

        actual = US_12(indi_repo._individual, indi_repo._family)

        self.assertEqual(actual, exp)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
