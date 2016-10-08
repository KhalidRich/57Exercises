# Test for character_count.py

import unittest
from character_count import lenmsg

class CharacterCountTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lenmsg(""), "There are no characters in this string.")

    def test_regular_string(self):
        self.assertEqual(lenmsg("four"), "'four' has 4 characters.")
        self.assertEqual(lenmsg("string with spaces"), "'string with spaces' has 18 characters.")
    
    def test_whitespace(self):
        self.assertEqual(lenmsg(" "), "' ' has 1 character.")

if __name__ == "__main__":
    unittest.main()
