import unittest
from INST326_Final_Project import *
class TestPasswordFunctions(unittest.TestCase):

    def test_password_length_checker(self):
        self.assertTrue(is_password_long_enough("12345678"))
        self.assertFalse(is_password_long_enough("12345"))

    def test_password_complexity_checker(self):
        self.assertFalse(is_password_complex("Password123"))

    def test_password_suggestion_generator(self):
        suggestions = password_suggestion_generator("kdo")
        self.assertIn("Try a longer password", suggestions)
        # print(suggestions)
        self.assertIn("Try adding numbers to increase complexity of password", suggestions)
        self.assertIn("Try adding uppercase to increase complexity of password", suggestions)

    def test_text_file_analyzer(self):
        strong_passwords, weak_passwords = text_file_analyzer("1000-most-common-passwords.csv")
        self.assertIn("Jackie72&$", strong_passwords )
        self.assertIn("brian", weak_passwords)


    def test_password_ranker(self):
        passwords = ["Password123", "weakpassword","strongP@ss"]

if __name__ == '__main__':
    unittest.main()
