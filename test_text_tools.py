import unittest
from text_tools import word_count

class TextTests(unittest.TestCase):
    def test_words(self):
        self.assertEqual(word_count("hello team"), 2)

    def test_blank(self):
        self.assertEqual(word_count("  "), 0)
