# Sample tests for Task:  "SORT ARRAY BY STRING LENGTH"
# Task description in SortArrayByStringLength.py module

import unittest
from SortArrayByStringLength import sort_by_length


class SortArrayByStringLengthTest(unittest.TestCase):
    def test_sort_by_length(self):
        self.assertEquals(sort_by_length(["i", "to", "beg", "life"]), ["beg", "life", "i", "to"])
        self.assertEquals(sort_by_length(["short", "longer", "longest"]), ["longer", "longest", "short"])
        self.assertEquals(sort_by_length(["", "pizza", "brains", "moderately"]), ["", "moderately", "brains", "pizza"])
        self.assertEquals(sort_by_length(["a", "of", "dog", "food"]), ["dog", "food", "a", "of"])
        self.assertEquals(sort_by_length(["", "bees", "eloquent", "dictionary"]), ["", "dictionary", "eloquent", "bees"])
        self.assertEquals(sort_by_length(["a short sentence", "a longer sentence", "the longest sentence"]),
                          ["a longer sentence", "the longest sentence", "a short sentence"])

# Command to execute the test in terminal: $ python -m unittest SortArrayByStringLengthTest.py
