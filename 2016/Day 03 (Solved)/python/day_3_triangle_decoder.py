""" Day 3 Advent of Code 2016 - Python Solution Attempt """

import re


class TriangleDecoder():

    @staticmethod
    def check_if_triangle_part_1(side1, side2, side3):

        if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
            return True
        else:
            return False

    @staticmethod
    def try_to_solve_day_3_part_1():
        input_file = open('input.txt', 'r')
        # print input_file.read()

        VALUES_IN_LINE_MATCHER = r'(\s+\d*)(\s+\d*)(\s+\d*)'
        total_valid_triangles = 0

        for line in input_file:
            # for each passed in line, get the three values via regex
            found_string = re.search(VALUES_IN_LINE_MATCHER, line)
            side1 = found_string.group(1)
            side2 = found_string.group(2)
            side3 = found_string.group(3)

            # clean the white space from the values
            side1 = side1.strip()
            side2 = side2.strip()
            side3 = side3.strip()

            # convert the strings to ints so math can be done
            side1_int = int(side1)
            side2_int = int(side2)
            side3_int = int(side3)

            # check if a valid triangle
            if TriangleDecoder.check_if_triangle_part_1(side1_int, side2_int, side3_int):
                total_valid_triangles += 1

        print "Total Number of Valid Triangles for Part 1 is: %d" % total_valid_triangles
        return total_valid_triangles

    @staticmethod
    def try_to_solve_day_3_part_2():
        input_file = open('input.txt', 'r')

        total_valid_triangles = 0

        first_column_list = []
        second_column_list = []
        third_column_list = []

        VALUES_IN_LINE_MATCHER = r'(\s+\d*)(\s+\d*)(\s+\d*)'

        for line in input_file:
            # for each passed in line, get the three values via regex
            found_string = re.search(VALUES_IN_LINE_MATCHER, line)
            side1 = found_string.group(1)
            side2 = found_string.group(2)
            side3 = found_string.group(3)

            # convert the strings to ints so math can be done
            side1_int = int(side1)
            side2_int = int(side2)
            side3_int = int(side3)

            # Add each side to the proper list so we can check at a time after adding all the lines to see if there are
            # valid triangles in each list and count the total
            first_column_list.append(side1_int)
            second_column_list.append(side2_int)
            third_column_list.append(side3_int)

        three_values_reached_list_one = False
        three_values_reached_total = 0
        list_one_three_sides_to_compare = []

        while not three_values_reached_list_one:
            for first_list_value in first_column_list:
                list_one_three_sides_to_compare.append(first_list_value)
                three_values_reached_total += 1

                if three_values_reached_total == 3:
                    # reset the loop so it checks the next three items
                    three_values_reached_total = 0

                    if TriangleDecoder.check_if_triangle_part_1(list_one_three_sides_to_compare[0],
                                                                list_one_three_sides_to_compare[1],
                                                                list_one_three_sides_to_compare[2]):
                        # check if current three sides are a valid triangle and if so, increment counter
                        total_valid_triangles += 1

                        # remove the current three sides to have a blank list again:
                        list_one_three_sides_to_compare = []
                    else:
                        # remove the current three sides to have a blank list again:
                        list_one_three_sides_to_compare = []

            # we're done the list so we need to stop the loop
            three_values_reached_list_one = True

        three_values_reached_list_two = False
        three_values_reached_total = 0
        list_two_three_sides_to_compare = []

        while not three_values_reached_list_two:
            for second_list_value in second_column_list:
                list_two_three_sides_to_compare.append(second_list_value)
                three_values_reached_total += 1

                if three_values_reached_total == 3:
                    # reset the loop so it checks the next three items
                    three_values_reached_total = 0

                    if TriangleDecoder.check_if_triangle_part_1(list_two_three_sides_to_compare[0],
                                                                list_two_three_sides_to_compare[1],
                                                                list_two_three_sides_to_compare[2]):
                        # check if current three sides are a valid triangle and if so, increment counter
                        total_valid_triangles += 1

                        # remove the current three sides to have a blank list again:
                        list_two_three_sides_to_compare = []
                    else:
                        # remove the current three sides to have a blank list again:
                        list_two_three_sides_to_compare = []

            # we're done the list so we need to stop the loop
            three_values_reached_list_two = True

        three_values_reached_list_three = False
        three_values_reached_total = 0
        list_three_three_sides_to_compare = []

        while not three_values_reached_list_three:
            for third_list_value in third_column_list:
                list_three_three_sides_to_compare.append(third_list_value)
                three_values_reached_total += 1

                if three_values_reached_total == 3:
                    # reset the loop so it checks the next three items
                    three_values_reached_total = 0

                    if TriangleDecoder.check_if_triangle_part_1(list_three_three_sides_to_compare[0],
                                                                list_three_three_sides_to_compare[1],
                                                                list_three_three_sides_to_compare[2]):
                        # check if current three sides are a valid triangle and if so, increment counter
                        total_valid_triangles += 1

                        # remove the current three sides to have a blank list again:
                        list_three_three_sides_to_compare = []
                    else:
                        # remove the current three sides to have a blank list again:
                        list_three_three_sides_to_compare = []

            # we're done the list so we need to stop the loop
            three_values_reached_list_three = True

        print "Total Number of Valid Triangles for Part 2 is: %d " % total_valid_triangles
        return total_valid_triangles
