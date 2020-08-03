import unittest
from src.main import *


class EmailValidation(unittest.TestCase):

    def test_positive_smtp_validation(self):
        self.assertTrue(smtp_validation("ghazalnoroozi27@gmail.com"))
        self.assertTrue(smtp_validation("gha.zal.noro.ozi27@gmail.com"))
        self.assertTrue(smtp_validation("ghazalnoroozi27@yahoo.com"))
        # self.assertTrue(smtp_validation("ghazalnoroozi27@aut.ac.ir"))

    def test_negative_smtp_validation(self):
        self.assertFalse(smtp_validation("hey__hi@hajakaja.com"))
        self.assertFalse(smtp_validation("vfghhnvbgfvfb@gmail.com"))

    def test_positive_regex_validation(self):
        self.assertTrue(regex_validation("email@example.com"))
        self.assertTrue(regex_validation("firstname.lastname@example.com"))
        self.assertTrue(regex_validation("email@subdomain.example.com"))
        self.assertTrue(regex_validation("firstname+lastname@example.com"))
        self.assertTrue(regex_validation("email@123.123.123.123"))
        self.assertTrue(regex_validation("1234567890@example.com"))
        self.assertTrue(regex_validation("email@example-one.com"))
        self.assertTrue(regex_validation("_______@example.com"))
        self.assertTrue(regex_validation("email@example.name"))
        self.assertTrue(regex_validation("email@example.museum"))
        self.assertTrue(regex_validation("email@example.co.jp"))
        self.assertTrue(regex_validation("firstname-lastname@example.com"))

    def test_negative_regex_validation(self):
        self.assertFalse(regex_validation("this\ is\"really\"not\allowed@example.com"))
        self.assertFalse(regex_validation("just”not”right@example.com"))
        self.assertFalse(regex_validation("(),:;<>[\]@example.com"))
        self.assertFalse(regex_validation("plainaddress"))
        self.assertFalse(regex_validation("#@%^%#$@#$@#.com"))
        self.assertFalse(regex_validation("@example.com"))
        self.assertFalse(regex_validation("Joe Smith <email@example.com>"))
        self.assertFalse(regex_validation("email.example.com"))
        self.assertFalse(regex_validation("email@example@example.com"))
        self.assertFalse(regex_validation("あいうえお@example.com"))
        self.assertFalse(regex_validation("email.@example"))


if __name__ == '__main__':
    unittest.main()
