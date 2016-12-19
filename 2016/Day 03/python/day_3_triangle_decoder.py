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
            # print line

            # for each passed in line, get the three values via regex
            found_string = re.search(VALUES_IN_LINE_MATCHER, line)
            side1 = found_string.group(1)
            side2 = found_string.group(2)
            side3 = found_string.group(3)

            # clean the white space from the values
            side1 = side1.strip()
            side2 = side2.strip()
            side3 = side3.strip()
            # print "side 1: " + str(side1)
            # print "side 2: " + str(side2)
            # print "side 3: " + str(side3)

            # convert the strings to ints so math can be done
            side1_int = int(side1)
            side2_int = int(side2)
            side3_int = int(side3)

            # check if a valid triangle
            if TriangleDecoder.check_if_triangle_part_1(side1_int, side2_int, side3_int):
                total_valid_triangles += 1

        print "Total Number of Valid Triangles from given input: %d" % total_valid_triangles
        return total_valid_triangles

    @staticmethod
    def check_if_triangle_part_2(side1, side2, side3):
        pass

    @staticmethod
    def try_to_solve_day_3_part_2():
        pass
