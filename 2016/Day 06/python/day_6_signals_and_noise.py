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
        elif c_common > a_common and c_common > b_common and c_common > d_common and c_common > e_common and \
            c_common > f_common and c_common > g_common and c_common > h_common and c_common > i_common and \
            c_common > j_common and c_common > k_common and c_common > l_common and c_common > m_common and \
            c_common > n_common and c_common > o_common and c_common > p_common and c_common > q_common and \
            c_common > r_common and c_common > s_common and c_common > t_common and c_common > u_common and \
            c_common > v_common and c_common > w_common and c_common > x_common and c_common > y_common and \
            c_common > z_common:
            columns_common_letter = c_common
        elif d_common > a_common and d_common > b_common and d_common > c_common and d_common > e_common and \
            d_common > f_common and d_common > g_common and d_common > h_common and d_common > i_common and \
            d_common > j_common and d_common > k_common and d_common > l_common and d_common > m_common and \
            d_common > n_common and d_common > o_common and d_common > p_common and d_common > q_common and \
            d_common > r_common and d_common > s_common and d_common > t_common and d_common > u_common and \
            d_common > v_common and d_common > w_common and d_common > x_common and d_common > y_common and \
            d_common > z_common:
            columns_common_letter = d_common
        elif e_common > a_common and e_common > b_common and e_common > c_common and e_common > d_common and \
            e_common > f_common and e_common > g_common and e_common > h_common and e_common > i_common and \
            e_common > j_common and e_common > k_common and e_common > l_common and e_common > m_common and \
            e_common > n_common and e_common > o_common and e_common > p_common and e_common > q_common and \
            e_common > r_common and e_common > s_common and e_common > t_common and e_common > u_common and \
            e_common > v_common and e_common > w_common and e_common > x_common and e_common > y_common and \
            e_common > z_common:
            columns_common_letter = e_common
        elif f_common > a_common and f_common > b_common and f_common > c_common and f_common > d_common and \
            f_common > e_common and f_common > g_common and f_common > h_common and f_common > i_common and \
            f_common > j_common and f_common > k_common and f_common > l_common and f_common > m_common and \
            f_common > n_common and f_common > o_common and f_common > p_common and f_common > q_common and \
            f_common > r_common and f_common > s_common and f_common > t_common and f_common > u_common and \
            f_common > v_common and f_common > w_common and f_common > x_common and f_common > y_common and \
            f_common > z_common:
            columns_common_letter = f_common
        elif g_common > a_common and g_common > b_common and g_common > c_common and g_common > d_common and \
            g_common > e_common and g_common > f_common and g_common > h_common and g_common > i_common and \
            g_common > j_common and g_common > k_common and g_common > l_common and g_common > m_common and \
            g_common > n_common and g_common > o_common and g_common > p_common and g_common > q_common and \
            g_common > r_common and g_common > s_common and g_common > t_common and g_common > u_common and \
            g_common > v_common and g_common > w_common and g_common > x_common and g_common > y_common and \
            g_common > z_common:
            columns_common_letter = g_common
        elif h_common > a_common and h_common > b_common and h_common > c_common and h_common > d_common and \
            h_common > e_common and h_common > f_common and h_common > g_common and h_common > i_common and \
            h_common > j_common and h_common > k_common and h_common > l_common and h_common > m_common and \
            h_common > n_common and h_common > o_common and h_common > p_common and h_common > q_common and \
            h_common > r_common and h_common > s_common and h_common > t_common and h_common > u_common and \
            h_common > v_common and h_common > w_common and h_common > x_common and h_common > y_common and \
            h_common > z_common:
            columns_common_letter = h_common
        elif i_common > a_common and i_common > b_common and i_common > c_common and i_common > d_common and \
            i_common > e_common and i_common > f_common and i_common > g_common and i_common > h_common and \
            i_common > j_common and i_common > k_common and i_common > l_common and i_common > m_common and \
            i_common > n_common and i_common > o_common and i_common > p_common and i_common > q_common and \
            i_common > r_common and i_common > s_common and i_common > t_common and i_common > u_common and \
            i_common > v_common and i_common > w_common and i_common > x_common and i_common > y_common and \
            i_common > z_common:
            columns_common_letter = i_common
        elif j_common > a_common and j_common > b_common and j_common > c_common and j_common > d_common and \
            j_common > e_common and j_common > f_common and j_common > g_common and j_common > h_common and \
            j_common > i_common and j_common > k_common and j_common > l_common and j_common > m_common and \
            j_common > n_common and j_common > o_common and j_common > p_common and j_common > q_common and \
            j_common > r_common and j_common > s_common and j_common > t_common and j_common > u_common and \
            j_common > v_common and j_common > w_common and j_common > x_common and j_common > y_common and \
            j_common > z_common:
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
