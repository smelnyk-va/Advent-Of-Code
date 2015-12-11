__author__ = 'smelnyk'

import unittest
from day2_code import order_more_wrapping_paper, calculate_footage_of_wrapping_paper_needed, order_more_ribbon, \
    calculate_footage_of_ribbon_needed


class Day2PartOneOrderMOreWrappingPaperTests(unittest.TestCase):
    def test_1x1x1_returns_6_Square_feet(self):
        result = order_more_wrapping_paper([1, 1, 1])
        self.assertEqual(7, result)

    def test_2x3x4_returns_58_square_feet_needed(self):
        result = order_more_wrapping_paper([2, 3, 4])
        self.assertEqual(58, result)

    def test_1x1x10_returns_43_square_feet_needed(self):
        result = order_more_wrapping_paper([1, 1, 10])
        self.assertEqual(43, result)

    def test_solve_day2_advent_of_code_for_me(self):
        result = order_more_wrapping_paper([3, 11, 24])
        # print "The Answer should be...: " + str(result) #Answer: 771
        self.assertEqual(771, result)


class Day2PartOneCalculateSquareFootageNeededTests(unittest.TestCase):
    def test_total_should_65(self):
        wrapping_paper_order_list = ['2x3x4', '1x1x10']
        result = calculate_footage_of_wrapping_paper_needed(wrapping_paper_order_list)
        print "The total should be: " + str(result)
        self.assertEqual(101, result)

    def test_calculate_first_two_answers_from_input(self):
        wrapping_paper_order_list = ['3x11x24', '13x5x19']
        result = calculate_footage_of_wrapping_paper_needed(wrapping_paper_order_list)
        # print "The total should be: " + str(result)
        self.assertEqual(1650, result)

    def test_answer_day2_for_me(self):
        wrapping_paper_order_list = open('input.txt', 'r')
        # print "wrapping_paper_order_list being looked at: " + str(wrapping_paper_order_list)
        result = calculate_footage_of_wrapping_paper_needed(wrapping_paper_order_list)
        # print "The total should be: " + str(result) # Answer: 1588178
        self.assertEqual(1588178, result)


class Day2PartTwoCalculateIndividualRibbonOrderTests(unittest.TestCase):
    def test_order_more_ribbon_single_order(self):  # 2x3x4
        ribbon_order = [2, 3, 4]
        result = order_more_ribbon(ribbon_order)
        # print "The total should be (34), got: " + str(result)
        self.assertEqual(34, result)

    def test_order_more_ribbon_single_order_two(self):  # 1x1x10
        ribbon_order = [1, 1, 10]
        result = order_more_ribbon(ribbon_order)
        # print "The total should be (14), got: " + str(result)
        self.assertEqual(14, result)

    def test_first_input_from_file(self):
        ribbon_order = [3, 11, 24]  # (3+3+11+11) + (3*11*24) = 28 + 792 = 820
        result = order_more_ribbon(ribbon_order)
        print "The total should be (820), got: " + str(result)
        self.assertEqual(820, result)

    def test_last_input_from_file(self):
        ribbon_order = [14, 6, 11]  # (6+6+11+11) + (14*6*11) = 34 + 924 = 958
        result = order_more_ribbon(ribbon_order)
        # print "The total should be (958), got: " + str(result)
        self.assertEqual(958, result)

    def test_larger_input_from_file(self):
        ribbon_order = [24, 25, 17]  # (17+17+24+24) + (24*25*17) = 82 + 10,200 = 10282
        result = order_more_ribbon(ribbon_order)
        print "The total should be (10282), got: " + str(result)
        self.assertEqual(10282, result)


class Day2PartTwoCalculateFootageOfRibbonNeededTests(unittest.TestCase):
    def test_get_full_order(self):  #
        full_order = ['2x3x4', '1x1x10']  # 34 + 14 = 48
        result = calculate_footage_of_ribbon_needed(full_order)
        # print "The total should be (48), got: " + str(result)
        self.assertEqual(48, result)

    def test_answer_day2_for_me(self):
        full_order = open('input.txt', 'r')
        result = calculate_footage_of_ribbon_needed(full_order)
        print "The total amount of ribbon needed should be: " + str(result)  # Answer: 3783758
        self.assertEqual(3783758, result)

        # TODO: Add more unit tests
