import unittest
from INST326_Final_Project import text_file_analyzer,password_suggestion_generator,password_complexity_checker,password_length_checker

class TestPasswordFunctions(unittest.TestCase):

    def test_password_length_checker(self):
        self.assertEqual(password_length_checker("12345678"), 8)
        self.assertEqual(password_length_checker("12345"), "Password does not meet length criteria (8 characters)")

    def test_password_complexity_checker(self):
        self.assertEqual(password_complexity_checker("Password123"), "Has uppercase True, has lowercase True, has number True,  has special character False")

    def test_password_suggestion_generator(self):
        suggestions = password_suggestion_generator("kd9")
        self.assertIn("Try a longer password", suggestions)
        self.assertIn("Try adding numbers to increase complexity of password", suggestions)
        self.assertIn("Try adding uppercase to increase complexity of password", suggestions)

    def test_text_file_analyzer(self):
        result = text_file_analyzer("100000-most-common-passwords.csv")
        self.assertIn("Your strong password:", result)
        self.assertIn("Your weak password:", result)


    def test_password_ranker(self):
        passwords = ["Password123", "weakpassword","strongP@ss"]
if __name__ == '__main__':
    unittest.main()
