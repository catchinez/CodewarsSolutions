# Sample tests for Task:  "JADEN CASING STRINGS"
# Task description in JadenCasingStrings.py module

import unittest
from JadenCasingStrings import to_jaden_case


class JadenCasingStringTest(unittest.TestCase):
    def test_string_equals(self):
        self.assertEquals(to_jaden_case("How can mirrors be real if our eyes aren't real"),
                          "How Can Mirrors Be Real If Our Eyes Aren't Real")

# Command to execute the test in terminal: $ python -m unittest JadenCasingStringTest.py
