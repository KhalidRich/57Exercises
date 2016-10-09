# Test printing_quotes.py

import unittest
from printing_quotes import format_quotes

class PrintingQuotesTest(unittest.TestCase):
    def test_empty_list(self):
        empty_msg = format_quotes([])
        self.assertEqual(empty_msg, "There are no quotes here.")

    def test_single_list(self):
        single_msg = format_quotes(self.singlet)
        self.assertEqual(single_msg, "Charles Dickens says, \"It was the best of times, it was the worst of times.\" ")

    def test_multi_list(self):
        multi_msg = format_quotes(self.multilet)
        self.assertEqual(multi_msg, "Charles Dickens says, \"It was the best of times, it was the worst of times.\" The Thing says, \"It's Clobberin' Time!\" ")

    def setUp(self):
        # set up some of the things we'll work with.
        for_both_lists = {"quote": "It was the best of times, it was the worst of times.", "author": "Charles Dickens"}
        for_multi_list = {"quote": "It's Clobberin' Time!", "author": "The Thing"}
        self.singlet = [for_both_lists]
        self.multilet = [for_both_lists, for_multi_list]

    def tearDown(self):
        # tear down the things we'll work with. just trying this out
        self.singlet = []
        self.multilet = []

if __name__ == "__main__":
    unittest.main()
