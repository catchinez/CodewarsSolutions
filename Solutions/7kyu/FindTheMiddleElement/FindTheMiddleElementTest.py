# Sample tests for Task:  "FIND THE MIDDLE ELEMENT"
# Task description in FindTheMiddleElement.py module

import unittest
from FindTheMiddleElement import gimme


class FindTheMiddleElementTest(unittest.TestCase):
    def test_gimme(self):
        self.assertEquals(gimme([2, 3, 1]), 0, 'Finds the index of middle element')
        self.assertEquals(gimme([5, 10, 14]), 1, 'Finds the index of middle element')

# Command to execute the test in terminal: $ python -m unittest FindTheMiddleElementTest.py
