""" Day 3 Advent of Code 2016 - Python Solution Attempt """

import re


class TriangleDecoder():

    @staticmethod
    def check_if_triangle(side1, side2, side3):

        if (side1 + side2) >= side3:
            return True
        # elif (side1 + side3) >= side2:
        #     return True
        # elif (side2 + side3) >= side1:
        #     return True
        else:
            return False

    @staticmethod
    def try_to_solve_day_3_part_1():
        input_file = open('input.txt', 'r')
        # print input_file.read()

        VALUES_IN_LINE_MATCHER = r'(\s+\d*)(\s+\d*)(\s+\d*)'
        total_triangles = 0

        for line in input_file:
            print line

            # for each passed in line, get the three values via regex
            found_string = re.search(VALUES_IN_LINE_MATCHER, line)
            side1 = found_string.group(1)
            side2 = found_string.group(2)
            side3 = found_string.group(3)

            # clean the white space from the values
            side1 = side1.strip()
            side2 = side2.strip()
            side3 = side3.strip()
            print "side 1: " + str(side1)
            print "side 2: " + str(side2)
            print "side 3: " + str(side3)

            # convert the strings to ints so math can be done
            side1_int = int(side1)
            side2_int = int(side2)
            side3_int = int(side3)

            # determine if a valid triangle
            # if (side1_int > side2_int + side3_int) or \
            #    (side2_int > side1_int + side3_int) or \
            #    (side3_int > side1_int + side2_int):
            #     print 'Not a triangle, sorry'
            # elif (side1_int == side2_int + side3_int) or \
            #      (side2_int == side1_int + side3_int) or \
            #      (side3_int == side1_int + side2_int):
            #     total_triangles = total_triangles + 1
            # else:
            #     total_triangles = total_triangles + 1

            if side1_int + side2_int > side3_int and side2_int + side3_int > side1_int and side3_int + side1_int > side2_int:
                total_triangles = total_triangles + 1

        return total_triangles
