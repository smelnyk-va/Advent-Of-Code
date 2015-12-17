__author__ = 'smelnyk'

import unittest
from day5_code import determine_if_string_has_three_vowels, get_total_of_nice_strings, \
    determine_if_at_least_one_letter_appears_twice_in_a_row_in_string, determine_if_string_has_ab_cd_pq_or_xy


class Day5Part1GetTotalOfNiceStringsTests(unittest.TestCase):

    def test_takes_in_multiple_strings(self):
        list_of_strings = open('input.txt', 'r')
        result = get_total_of_nice_strings(list_of_strings)
        # self.assertEqual(2, result)
        print "The Answer to Day 5, Part 1 is: " + str(result)


class Day5Part1DetermineIfStringHasThreeVowelsTests(unittest.TestCase):

    def test_contains_at_least_three_vowels(self):
        result = determine_if_string_has_three_vowels('aei')
        self.assertEqual(1, result)

    def test_contains_at_least_three_vowels_two(self):
        result = determine_if_string_has_three_vowels('xazegov')
        self.assertEqual(1, result)

    def test_contains_at_least_three_vowels_three(self):
        result = determine_if_string_has_three_vowels('aeiouaeiouaeiou')
        self.assertEqual(1, result)

    def test_does_not_contain_at_least_three_vowels_only_1_vowel(self):
        result = determine_if_string_has_three_vowels('dvszwmarrgswjxmb') #has only 1 vowel
        self.assertEqual(0, result)

    def test_does_not_contain_at_least_three_vowels_has_only_2_vowels(self):
        result = determine_if_string_has_three_vowels('dvsziwmarrgswjxb') #has only 2 vowels
        self.assertEqual(0, result)


class Day5Part1DetermineIfAtLeastOneLetterAppearsTwiceInARowTests(unittest.TestCase):

    def test_does_contain_1_letter_that_appears_twice_in_a_row_shortest_test(self):
        result = determine_if_at_least_one_letter_appears_twice_in_a_row_in_string('xx')
        self.assertEqual(1, result)

    def test_does_contain_1_letter_that_appears_twice_in_a_row_short_test(self):
        result = determine_if_at_least_one_letter_appears_twice_in_a_row_in_string('abcdde')
        self.assertEqual(1, result)

    def test_does_contain_1_letter_that_appears_twice_in_a_row_multiple_times(self):
        result = determine_if_at_least_one_letter_appears_twice_in_a_row_in_string('aabbccdd')
        self.assertEqual(1, result)

    def test_does_contain_1_letter_that_appears_twice_in_a_row_long_test(self):
        result = determine_if_at_least_one_letter_appears_twice_in_a_row_in_string('kpvwblrizaabmnhz')
        self.assertEqual(1, result)

    def test_does_not_contain_1_letter_that_appears_twice_in_a_row_long_test(self):
        result = determine_if_at_least_one_letter_appears_twice_in_a_row_in_string('kpvwblrizawbmnhz')
        self.assertEqual(0, result)


class Day5Part1DetermineIfStringHasAbCdPqXyTests(unittest.TestCase):

    def test_does_contain_ab_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('kpvwblrizaabmnhz')
        self.assertEqual(0, result)

    def test_does_not_contain_ab_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('zetxvrgjmblxvakr')
        self.assertEqual(1, result)

    def test_does_contain_cd_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('tfetfqojqcdzlpbm')
        self.assertEqual(0, result)

    def test_does_not_contain_cd_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('qpnxkuldeiituggg')
        self.assertEqual(1, result)

    def test_does_contain_pq_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('ydjyboqwhfpqfydc')
        self.assertEqual(0, result)

    def test_does_not_contain_pq_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('dwhttezyanrnbybv')
        self.assertEqual(1, result)

    def test_does_contain_xy_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('haegwjzuvuyypxyu')
        self.assertEqual(0, result)

    def test_does_not_contain_xy_in_string(self):
        result = determine_if_string_has_ab_cd_pq_or_xy('haegxwjzuvuyypyu')
        self.assertEqual(1, result)



