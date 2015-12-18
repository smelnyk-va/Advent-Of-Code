__author__ = 'smelnyk'

import unittest
from day5_code import determine_if_string_has_three_vowels, get_total_of_nice_strings, \
    determine_if_at_least_one_letter_appears_twice_in_a_row_in_string, determine_if_string_has_ab_cd_pq_or_xy, \
    one_function_to_do_it_all_part_1, one_function_to_do_it_all_part_2, \
    determine_if_string_has_2_letters_that_appear_twice_without_overlap, \
    determine_if_string_contains_at_least_one_letter_which_repeats


class Day5Part2OneFunctionToDoPart2AllTests(unittest.TestCase):

    def test_solve_day_5_part_2_for_me(self):
        list_of_strings = open('input.txt', 'r')
        result = one_function_to_do_it_all_part_2(list_of_strings)
        print "The Answer to Day 5, Part 2 is: " + str(result)  # Answer: 55
        # self.assertEqual(55, result)

    def test_should_pass_all_three_rules_for_only_2(self):
        list_of_strings = open('testinputpart2.txt', 'r')
        result = one_function_to_do_it_all_part_2(list_of_strings)
        self.assertEqual(2, result)
        # print "The answer is: " + str(result)


class Day5Part2DetermineIfStringHas2LettersThatAppearTwiceWithoutOverlapTests(unittest.TestCase):

    def test_string_has_2_letters_first_example(self):
        result = determine_if_string_has_2_letters_that_appear_twice_without_overlap('xyxy')
        self.assertEqual(1, result)

    def test_string_has_2_letters_second_example(self):
        result = determine_if_string_has_2_letters_that_appear_twice_without_overlap('aabcdefgaa')
        self.assertEqual(1, result)

    def test_string_does_not_have_2_letters_has_overlap_third_example(self):
        result = determine_if_string_has_2_letters_that_appear_twice_without_overlap('aaa')
        self.assertEqual(0, result)


class Day5Part2DetermineIfStringContainsAtLeastOneLetterWhichRepeatsTests(unittest.TestCase):

    def test_string_contains_a_repeating_character_first_example(self):
        result = determine_if_string_contains_at_least_one_letter_which_repeats('xyx')
        self.assertEqual(1, result)

    def test_string_contains_a_repeating_character_second_example(self):
        result = determine_if_string_contains_at_least_one_letter_which_repeats('abcdefeghi')
        self.assertEqual(1, result)

    def test_string_contains_a_repeating_character_third_example(self):
        result = determine_if_string_contains_at_least_one_letter_which_repeats('aaa')
        self.assertEqual(1, result)


class Day5Part1OneFunctionToDoAllPart1Tests(unittest.TestCase):

    def test_solve_day_5_part_1_for_me(self):
        list_of_strings = open('input.txt', 'r')
        result = one_function_to_do_it_all_part_1(list_of_strings)
        self.assertEqual(255, result)
        # print "The Answer to Day 5, Part 1 is: " + str(result)  # Answer: 255

    def test_should_pass_all_three_rules_for_only_2(self):
        list_of_strings = open('testinputpart1.txt', 'r')
        result = one_function_to_do_it_all_part_1(list_of_strings)
        self.assertEqual(2, result)
        # print "The answer is: " + str(result)


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



