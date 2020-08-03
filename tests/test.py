import unittest
from src.main import *


class EmailValidation(unittest.TestCase):

    def test_positive_smtp_validation(self):
        self.assertTrue(smtp_validation("ghazalnoroozi27@gmail.com"))
        # self.assertTrue(smtp_validation("ghazalnoroozi27@aut.ac.ir"))
        self.assertTrue(smtp_validation("ghazalnoroozi27@yahoo.com"))
        self.assertTrue(smtp_validation("gha.zal.noro.ozi27@gmail.com"))

    def test_negative_smtp_validation(self):
        self.assertFalse(smtp_validation("hey__hi@haja.com"))
        self.assertFalse(smtp_validation("vfghhnvbgfvfb@gmail.com"))

    def test_positive_regex_validation(self):
        self.assertTrue(regex_validation("ghazalnoroozi27@gmail.com"))
        self.assertTrue(regex_validation("ghazalnoroozi27@aut.ac.ir"))
        self.assertTrue(regex_validation("ghazalnoroozi27@yahoo.com"))

    def test_negative_regex_validation(self):
        self.assertFalse(regex_validation("higmail.com"))
        # self.assertFalse(regex_validation("hey__there@gmail.com"))


if __name__ == '__main__':
    unittest.main()
