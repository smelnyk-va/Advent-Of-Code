""" Day 3 Advent of Code 2016 - Python Solution Attempt """


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

        total_triangles = 0
        # is_triangle = False

        for line in input_file:
            print line
            emptyspace, side1, emptyspace1, side2, emptyspace2, side3, emptyspace3 = line.split('  ')
            # print "side 1: %d" % int(side1)
            print "emptyspace: " + str(emptyspace)
            print "side 1: " + str(side1)
            print "side 2: " + str(side2)
            print "side 3: " + str(side3)
            side1_int = int(side1)
            side2_int = int(side2)
            side3_int = int(side3)

            if (side1_int + side2_int) >= side3_int:
                # is_triangle = True
                total_triangles+1
            # else:
                # is_triangle = False

        return total_triangles
