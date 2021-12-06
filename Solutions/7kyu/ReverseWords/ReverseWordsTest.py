# Sample tests for Task:  "REVERSE WORDS"
# Task description in JadenCasingStrings.py module

import unittest
from ReverseWords import reverse_words


class JadenCasingStringTest(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEquals(reverse_words('The quick brown fox jumps over the lazy dog.'),
                          'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEquals(reverse_words('apple'), 'elppa')
        self.assertEquals(reverse_words('a b c d'), 'a b c d')
        self.assertEquals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')

# Command to execute the test in terminal: $ python -m unittest ReverseWordsTest.py
