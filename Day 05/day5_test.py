__author__ = 'smelnyk'

import unittest
from day5_code import find_number_strings_that_are_nice

class Day5Part1Tests(unittest.TestCase):

    def test_contains_at_least_three_vowels(self):
        result = find_number_strings_that_are_nice('aei')
        self.assertEqual(1, result)

    def test_contains_at_least_three_vowels_two(self):
        result = find_number_strings_that_are_nice('xazegov')
        self.assertEqual(1, result)

    def test_contains_at_least_three_vowels_three(self):
        result = find_number_strings_that_are_nice('aeiouaeiouaeiou')
        self.assertEqual(1, result)

    def test_does_not_contain_at_least_three_vowels(self):
        result = find_number_strings_that_are_nice('hello')
        self.assertEqual(0, result)