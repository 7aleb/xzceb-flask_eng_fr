"""Module providingFunction printing python version."""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """class to test translation"""
    def test_english_to_french(self):
        """Function translating en to fr."""
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

    def test_french_to_english(self):
        """Function translating fr to en."""
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
    