""" Day 6 Advent of Code 2016 - Python Solution Attempt """

import re


class SignalsAndNoise:

    def __init__(self):
        pass

    @staticmethod
    def calculate_most_common_letter_of_the_given_column_return_combined_string(
            column_1_list, column_2_list, column_3_list, column_4_list, column_5_list,
            column_6_list, column_7_list, column_8_list):

        column_1_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_1_list)
        column_2_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_2_list)
        column_3_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_3_list)
        column_4_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_4_list)
        column_5_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_5_list)
        column_6_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_6_list)
        column_7_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_7_list)
        column_8_most_common = SignalsAndNoise.calculate_most_common_letter_of_given_list(column_8_list)

        most_string_combined = column_1_most_common + column_2_most_common + column_3_most_common + \
                               column_4_most_common + column_5_most_common + column_6_most_common + \
                               column_7_most_common + column_8_most_common

        return most_string_combined

    @staticmethod
    def calculate_most_common_letter_of_given_list(column_list):
        columns_common_letter = ''

        a_common = 0
        b_common = 0
        c_common = 0
        d_common = 0
        e_common = 0
        f_common = 0
        g_common = 0
        h_common = 0
        i_common = 0
        j_common = 0
        k_common = 0
        l_common = 0
        m_common = 0
        n_common = 0
        o_common = 0
        p_common = 0
        q_common = 0
        r_common = 0
        s_common = 0
        t_common = 0
        u_common = 0
        v_common = 0
        w_common = 0
        x_common = 0
        y_common = 0
        z_common = 0

        # sort the list first
        column_list = column_list.sort()

        for letter in column_list:
            if letter == 'a':
                a_common += 1
            elif letter == 'b':
                b_common += 1
            elif letter == 'c':
                c_common += 1
            elif letter == 'd':
                d_common += 1
            elif letter == 'e':
                e_common += 1
            elif letter == 'f':
                f_common += 1
            elif letter == 'g':
                g_common += 1
            elif letter == 'h':
                h_common += 1
            elif letter == 'i':
                i_common += 1
            elif letter == 'j':
                j_common += 1
            elif letter == 'k':
                k_common += 1
            elif letter == 'l':
                l_common += 1
            elif letter == 'm':
                m_common += 1
            elif letter == 'n':
                n_common += 1
            elif letter == 'o':
                o_common += 1
            elif letter == 'p':
                p_common += 1
            elif letter == 'q':
                q_common += 1
            elif letter == 'r':
                r_common += 1
            elif letter == 's':
                s_common += 1
            elif letter == 't':
                t_common += 1
            elif letter == 'u':
                u_common += 1
            elif letter == 'v':
                v_common += 1
            elif letter == 'w':
                w_common += 1
            elif letter == 'x':
                x_common += 1
            elif letter == 'y':
                y_common += 1
            elif letter == 'z':
                z_common += 1

        if a_common > b_common and a_common > c_common and a_common > d_common and a_common > e_common and \
            a_common > f_common and a_common > g_common and a_common > h_common and a_common > i_common and \
            a_common > j_common and a_common > k_common and a_common > l_common and a_common > m_common and \
            a_common > n_common and a_common > o_common and a_common > p_common and a_common > q_common and \
            a_common > r_common and a_common > s_common and a_common > t_common and a_common > u_common and \
            a_common > v_common and a_common > w_common and a_common > x_common and a_common > y_common and \
            a_common > z_common:
            columns_common_letter = a_common
        elif b_common > a_common and b_common > c_common and b_common > d_common and b_common > e_common and \
            b_common > f_common and b_common > g_common and b_common > h_common and b_common > i_common and \
            b_common > j_common and b_common > k_common and b_common > l_common and b_common > m_common and \
            b_common > n_common and b_common > o_common and b_common > p_common and b_common > q_common and \
            b_common > r_common and b_common > s_common and b_common > t_common and b_common > u_common and \
            b_common > v_common and b_common > w_common and b_common > x_common and b_common > y_common and \
            b_common > z_common:
            columns_common_letter = b_common
        elif :
            columns_common_letter = c_common
        elif :
            columns_common_letter = d_common
        elif :
            columns_common_letter = e_common
        elif :
            columns_common_letter = f_common
        elif :
            columns_common_letter = g_common
        elif :
            columns_common_letter = h_common
        elif :
            columns_common_letter = i_common
        elif :
            columns_common_letter = j_common
        elif :
            columns_common_letter = k_common
        elif :
            columns_common_letter = l_common
        elif :
            columns_common_letter = m_common
        elif :
            columns_common_letter = n_common
        elif :
            columns_common_letter = o_common
        elif :
            columns_common_letter = p_common
        elif :
            columns_common_letter = q_common
        elif :
            columns_common_letter = r_common
        elif :
            columns_common_letter = s_common
        elif :
            columns_common_letter = t_common
        elif :
            columns_common_letter = u_common
        elif :
            columns_common_letter = v_common
        elif :
            columns_common_letter = w_common
        elif :
            columns_common_letter = x_common
        elif :
            columns_common_letter = y_common
        else:
            columns_common_letter = z_common
        return columns_common_letter

    def day_6_signals_and_noise_part_1(self):
        input_file = open('input.txt', 'r')

        column_1_list = []
        column_2_list = []
        column_3_list = []
        column_4_list = []
        column_5_list = []
        column_6_list = []
        column_7_list = []
        column_8_list = []

        LETTERS_IN_LINE_MATCHER = r'(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)'

        for line in input_file:
            # for each passed in line, get the 8 letters via regex
            found_letters_string = re.search(LETTERS_IN_LINE_MATCHER, line)
            first_letter = found_letters_string.group(1)
            second_letter = found_letters_string.group(2)
            third_letter = found_letters_string.group(3)
            fourth_letter = found_letters_string.group(4)
            fifth_letter = found_letters_string.group(5)
            sixth_letter = found_letters_string.group(6)
            seventh_letter = found_letters_string.group(7)
            eigth_letter = found_letters_string.group(8)

            # add each letter to it's corresponding list
            column_1_list.append(first_letter)
            column_2_list.append(second_letter)
            column_3_list.append(third_letter)
            column_4_list.append(fourth_letter)
            column_5_list.append(fifth_letter)
            column_6_list.append(sixth_letter)
            column_7_list.append(seventh_letter)
            column_8_list.append(eigth_letter)

        # once the whole input file has been separated into columns, pass it along into the
        # helper function to loop through them to get the common letter in each list
        day_6_part_1_answer = SignalsAndNoise. \
            calculate_most_common_letter_of_the_given_column_return_combined_string(column_1_list,
                                                                              column_2_list,
                                                                              column_3_list,
                                                                              column_4_list,
                                                                              column_5_list,
                                                                              column_6_list,
                                                                              column_7_list,
                                                                              column_8_list)
        print "Day 6 Part 1 Answer: " + day_6_part_1_answer
        return day_6_part_1_answer
