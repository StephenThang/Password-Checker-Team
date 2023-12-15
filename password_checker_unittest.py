import unittest
from password_checker import *
"""
Unit test for password checking functions

Includes tests for various aspects of password security

Covers tests for length, complexity, suggestions, text file analysis for strength, and password ranking

Each test ensures the function behaves as expected under given conditions
"""
class TestPasswordFunctions(unittest.TestCase):

    def test_password_length_checker(self): # Test cases for verifying password length
        self.assertTrue(is_password_long_enough("12345678"))
        self.assertFalse(is_password_long_enough("12345"))

    def test_password_complexity_checker(self): # Test cases for verifying password complexity
        self.assertFalse(is_password_complex("Password123"))

    def test_password_suggestion_generator(self): # Test cases for generating password suggestions
        suggestions = password_suggestion_generator("kdo")
        self.assertIn("Try a longer password", suggestions)
        self.assertIn("Try adding numbers to increase complexity of password", suggestions)
        self.assertIn("Try adding upper case letters to increase complexity of password", suggestions)

    def test_text_file_analyzer(self): # Test cases for analyzing passwords in a text file
        strong_passwords, weak_passwords = text_file_analyzer("1000-most-common-passwords.csv")
        self.assertIn("Jackie72&$", strong_passwords )
        self.assertIn("brian", weak_passwords)

    def test_password_ranker(self): # Test cases for ranking multiple passwords
        passwords = ["Password123", "weakpassword","strongP@ss33", "st*&rongP@ss87"]
        correct_output = ["st*&rongP@ss87", "strongP@ss33","Password123", "weakpassword"]
        self.assertEqual(password_ranker(passwords), correct_output)

if __name__ == '__main__':
    unittest.main()
