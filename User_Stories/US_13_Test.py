import unittest
from US_13 import US_13
from Base_Files.Repository import Repository



class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_13(self):
        """ The function helps to test US_13 function"""
        indi_repo: Repository = Repository("../GEDCOM_Files/US_02.ged")
        expected = {'The family id @F13@ has twins Emmy /Robinson/ and Bholu /Desai/ and Line number: 508',
                    'The family id @F13@ has twins Jil /Robinson/ and Bholu /Desai/ and Line number: 508',
                    'The family id @F13@ has twins Emmy /Robinson/ and Jil /Robinson/ and Line number: 508'}

        actual = US_13(indi_repo._family, indi_repo._individual)

        print(actual)

        self.assertEqual(actual, expected)
    
        

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
