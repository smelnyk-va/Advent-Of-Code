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
        column_list.sort()
        print column_list

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
            columns_common_letter = 'a'
        elif b_common > a_common and b_common > c_common and b_common > d_common and b_common > e_common and \
            b_common > f_common and b_common > g_common and b_common > h_common and b_common > i_common and \
            b_common > j_common and b_common > k_common and b_common > l_common and b_common > m_common and \
            b_common > n_common and b_common > o_common and b_common > p_common and b_common > q_common and \
            b_common > r_common and b_common > s_common and b_common > t_common and b_common > u_common and \
            b_common > v_common and b_common > w_common and b_common > x_common and b_common > y_common and \
            b_common > z_common:
            columns_common_letter = 'b'
        elif c_common > a_common and c_common > b_common and c_common > d_common and c_common > e_common and \
            c_common > f_common and c_common > g_common and c_common > h_common and c_common > i_common and \
            c_common > j_common and c_common > k_common and c_common > l_common and c_common > m_common and \
            c_common > n_common and c_common > o_common and c_common > p_common and c_common > q_common and \
            c_common > r_common and c_common > s_common and c_common > t_common and c_common > u_common and \
            c_common > v_common and c_common > w_common and c_common > x_common and c_common > y_common and \
            c_common > z_common:
            columns_common_letter = 'c'
        elif d_common > a_common and d_common > b_common and d_common > c_common and d_common > e_common and \
            d_common > f_common and d_common > g_common and d_common > h_common and d_common > i_common and \
            d_common > j_common and d_common > k_common and d_common > l_common and d_common > m_common and \
            d_common > n_common and d_common > o_common and d_common > p_common and d_common > q_common and \
            d_common > r_common and d_common > s_common and d_common > t_common and d_common > u_common and \
            d_common > v_common and d_common > w_common and d_common > x_common and d_common > y_common and \
            d_common > z_common:
            columns_common_letter = 'd'
        elif e_common > a_common and e_common > b_common and e_common > c_common and e_common > d_common and \
            e_common > f_common and e_common > g_common and e_common > h_common and e_common > i_common and \
            e_common > j_common and e_common > k_common and e_common > l_common and e_common > m_common and \
            e_common > n_common and e_common > o_common and e_common > p_common and e_common > q_common and \
            e_common > r_common and e_common > s_common and e_common > t_common and e_common > u_common and \
            e_common > v_common and e_common > w_common and e_common > x_common and e_common > y_common and \
            e_common > z_common:
            columns_common_letter = 'e'
        elif f_common > a_common and f_common > b_common and f_common > c_common and f_common > d_common and \
            f_common > e_common and f_common > g_common and f_common > h_common and f_common > i_common and \
            f_common > j_common and f_common > k_common and f_common > l_common and f_common > m_common and \
            f_common > n_common and f_common > o_common and f_common > p_common and f_common > q_common and \
            f_common > r_common and f_common > s_common and f_common > t_common and f_common > u_common and \
            f_common > v_common and f_common > w_common and f_common > x_common and f_common > y_common and \
            f_common > z_common:
            columns_common_letter = 'f'
        elif g_common > a_common and g_common > b_common and g_common > c_common and g_common > d_common and \
            g_common > e_common and g_common > f_common and g_common > h_common and g_common > i_common and \
            g_common > j_common and g_common > k_common and g_common > l_common and g_common > m_common and \
            g_common > n_common and g_common > o_common and g_common > p_common and g_common > q_common and \
            g_common > r_common and g_common > s_common and g_common > t_common and g_common > u_common and \
            g_common > v_common and g_common > w_common and g_common > x_common and g_common > y_common and \
            g_common > z_common:
            columns_common_letter = 'g'
        elif h_common > a_common and h_common > b_common and h_common > c_common and h_common > d_common and \
            h_common > e_common and h_common > f_common and h_common > g_common and h_common > i_common and \
            h_common > j_common and h_common > k_common and h_common > l_common and h_common > m_common and \
            h_common > n_common and h_common > o_common and h_common > p_common and h_common > q_common and \
            h_common > r_common and h_common > s_common and h_common > t_common and h_common > u_common and \
            h_common > v_common and h_common > w_common and h_common > x_common and h_common > y_common and \
            h_common > z_common:
            columns_common_letter = 'h'
        elif i_common > a_common and i_common > b_common and i_common > c_common and i_common > d_common and \
            i_common > e_common and i_common > f_common and i_common > g_common and i_common > h_common and \
            i_common > j_common and i_common > k_common and i_common > l_common and i_common > m_common and \
            i_common > n_common and i_common > o_common and i_common > p_common and i_common > q_common and \
            i_common > r_common and i_common > s_common and i_common > t_common and i_common > u_common and \
            i_common > v_common and i_common > w_common and i_common > x_common and i_common > y_common and \
            i_common > z_common:
            columns_common_letter = 'i'
        elif j_common > a_common and j_common > b_common and j_common > c_common and j_common > d_common and \
            j_common > e_common and j_common > f_common and j_common > g_common and j_common > h_common and \
            j_common > i_common and j_common > k_common and j_common > l_common and j_common > m_common and \
            j_common > n_common and j_common > o_common and j_common > p_common and j_common > q_common and \
            j_common > r_common and j_common > s_common and j_common > t_common and j_common > u_common and \
            j_common > v_common and j_common > w_common and j_common > x_common and j_common > y_common and \
            j_common > z_common:
            columns_common_letter = 'j'
        elif k_common > a_common and k_common > b_common and k_common > c_common and k_common > d_common and \
            k_common > e_common and k_common > f_common and k_common > g_common and k_common > h_common and \
            k_common > i_common and k_common > j_common and k_common > l_common and k_common > m_common and \
            k_common > n_common and k_common > o_common and k_common > p_common and k_common > q_common and \
            k_common > r_common and k_common > s_common and k_common > t_common and k_common > u_common and \
            k_common > v_common and k_common > w_common and k_common > x_common and k_common > y_common and \
            k_common > z_common:
            columns_common_letter = 'k'
        elif l_common > a_common and l_common > b_common and l_common > c_common and l_common > d_common and \
            l_common > e_common and l_common > f_common and l_common > g_common and l_common > h_common and \
            l_common > i_common and l_common > j_common and l_common > k_common and l_common > m_common and \
            l_common > n_common and l_common > o_common and l_common > p_common and l_common > q_common and \
            l_common > r_common and l_common > s_common and l_common > t_common and l_common > u_common and \
            l_common > v_common and l_common > w_common and l_common > x_common and l_common > y_common and \
            l_common > z_common:
            columns_common_letter = 'l'
        elif m_common > a_common and m_common > b_common and m_common > c_common and m_common > d_common and \
            m_common > e_common and m_common > f_common and m_common > g_common and m_common > h_common and \
            m_common > i_common and m_common > j_common and m_common > k_common and m_common > l_common and \
            m_common > n_common and m_common > o_common and m_common > p_common and m_common > q_common and \
            m_common > r_common and m_common > s_common and m_common > t_common and m_common > u_common and \
            m_common > v_common and m_common > w_common and m_common > x_common and m_common > y_common and \
            m_common > z_common:
            columns_common_letter = 'm'
        elif n_common > a_common and n_common > b_common and n_common > c_common and n_common > d_common and \
            n_common > e_common and n_common > f_common and n_common > g_common and n_common > h_common and \
            n_common > i_common and n_common > j_common and n_common > k_common and n_common > l_common and \
            n_common > m_common and n_common > o_common and n_common > p_common and n_common > q_common and \
            n_common > r_common and n_common > s_common and n_common > t_common and n_common > u_common and \
            n_common > v_common and n_common > w_common and n_common > x_common and n_common > y_common and \
            n_common > z_common:
            columns_common_letter = 'n'
        elif o_common > a_common and o_common > b_common and o_common > c_common and o_common > d_common and \
            o_common > e_common and o_common > f_common and o_common > g_common and o_common > h_common and \
            o_common > i_common and o_common > j_common and o_common > k_common and o_common > l_common and \
            o_common > m_common and o_common > n_common and o_common > p_common and o_common > q_common and \
            o_common > r_common and o_common > s_common and o_common > t_common and o_common > u_common and \
            o_common > v_common and o_common > w_common and o_common > x_common and o_common > y_common and \
            o_common > z_common:
            columns_common_letter = 'o'
        elif p_common > a_common and p_common > b_common and p_common > c_common and p_common > d_common and \
            p_common > e_common and p_common > f_common and p_common > g_common and p_common > h_common and \
            p_common > i_common and p_common > j_common and p_common > k_common and p_common > l_common and \
            p_common > m_common and p_common > n_common and p_common > o_common and p_common > q_common and \
            p_common > r_common and p_common > s_common and p_common > t_common and p_common > u_common and \
            p_common > v_common and p_common > w_common and p_common > x_common and p_common > y_common and \
            p_common > z_common:
            columns_common_letter = 'p'
        elif q_common > a_common and q_common > b_common and q_common > c_common and q_common > d_common and \
            q_common > e_common and q_common > f_common and q_common > g_common and q_common > h_common and \
            q_common > i_common and q_common > j_common and q_common > k_common and q_common > l_common and \
            q_common > m_common and q_common > n_common and q_common > o_common and q_common > p_common and \
            q_common > r_common and q_common > s_common and q_common > t_common and q_common > u_common and \
            q_common > v_common and q_common > w_common and q_common > x_common and q_common > y_common and \
            q_common > z_common:
            columns_common_letter = 'q'
        elif r_common > a_common and r_common > b_common and r_common > c_common and r_common > d_common and \
            r_common > e_common and r_common > f_common and r_common > g_common and r_common > h_common and \
            r_common > i_common and r_common > j_common and r_common > k_common and r_common > l_common and \
            r_common > m_common and r_common > n_common and r_common > o_common and r_common > p_common and \
            r_common > q_common and r_common > s_common and r_common > t_common and r_common > u_common and \
            r_common > v_common and r_common > w_common and r_common > x_common and r_common > y_common and \
            r_common > z_common:
            columns_common_letter = 'r'
        elif s_common > a_common and s_common > b_common and s_common > c_common and s_common > d_common and \
            s_common > e_common and s_common > f_common and s_common > g_common and s_common > h_common and \
            s_common > i_common and s_common > j_common and s_common > k_common and s_common > l_common and \
            s_common > m_common and s_common > n_common and s_common > o_common and s_common > p_common and \
            s_common > q_common and s_common > r_common and s_common > t_common and s_common > u_common and \
            s_common > v_common and s_common > w_common and s_common > x_common and s_common > y_common and \
            s_common > z_common:
            columns_common_letter = 's'
        elif t_common > a_common and t_common > b_common and t_common > c_common and t_common > d_common and \
            t_common > e_common and t_common > f_common and t_common > g_common and t_common > h_common and \
            t_common > i_common and t_common > j_common and t_common > k_common and t_common > l_common and \
            t_common > m_common and t_common > n_common and t_common > o_common and t_common > p_common and \
            t_common > q_common and t_common > r_common and t_common > s_common and t_common > u_common and \
            t_common > v_common and t_common > w_common and t_common > x_common and t_common > y_common and \
            t_common > z_common:
            columns_common_letter = 't'
        elif u_common > a_common and u_common > b_common and u_common > c_common and u_common > d_common and \
            u_common > e_common and u_common > f_common and u_common > g_common and u_common > h_common and \
            u_common > i_common and u_common > j_common and u_common > k_common and u_common > l_common and \
            u_common > m_common and u_common > n_common and u_common > o_common and u_common > p_common and \
            u_common > q_common and u_common > r_common and u_common > s_common and u_common > t_common and \
            u_common > v_common and u_common > w_common and u_common > x_common and u_common > y_common and \
            u_common > z_common:
            columns_common_letter = 'u'
        elif v_common > a_common and v_common > b_common and v_common > c_common and v_common > d_common and \
            v_common > e_common and v_common > f_common and v_common > g_common and v_common > h_common and \
            v_common > i_common and v_common > j_common and v_common > k_common and v_common > l_common and \
            v_common > m_common and v_common > n_common and v_common > o_common and v_common > p_common and \
            v_common > q_common and v_common > r_common and v_common > s_common and v_common > t_common and \
            v_common > u_common and v_common > w_common and v_common > x_common and v_common > y_common and \
            v_common > z_common:
            columns_common_letter = 'v'
        elif w_common > a_common and w_common > b_common and w_common > c_common and w_common > d_common and \
            w_common > e_common and w_common > f_common and w_common > g_common and w_common > h_common and \
            w_common > i_common and w_common > j_common and w_common > k_common and w_common > l_common and \
            w_common > m_common and w_common > n_common and w_common > o_common and w_common > p_common and \
            w_common > q_common and w_common > r_common and w_common > s_common and w_common > t_common and \
            w_common > u_common and w_common > v_common and w_common > x_common and w_common > y_common and \
            w_common > z_common:
            columns_common_letter = 'w'
        elif x_common > a_common and x_common > b_common and x_common > c_common and x_common > d_common and \
            x_common > e_common and x_common > f_common and x_common > g_common and x_common > h_common and \
            x_common > i_common and x_common > j_common and x_common > k_common and x_common > l_common and \
            x_common > m_common and x_common > n_common and x_common > o_common and x_common > p_common and \
            x_common > q_common and x_common > r_common and x_common > s_common and x_common > t_common and \
            x_common > u_common and x_common > v_common and x_common > w_common and x_common > y_common and \
            x_common > z_common:
            columns_common_letter = 'x'
        elif y_common > a_common and y_common > b_common and y_common > c_common and y_common > d_common and \
            y_common > e_common and y_common > f_common and y_common > g_common and y_common > h_common and \
            y_common > i_common and y_common > j_common and y_common > k_common and y_common > l_common and \
            y_common > m_common and y_common > n_common and y_common > o_common and y_common > p_common and \
            y_common > q_common and y_common > r_common and y_common > s_common and y_common > t_common and \
            y_common > u_common and y_common > v_common and y_common > w_common and y_common > x_common and \
            y_common > z_common:
            columns_common_letter = 'y'
        else:
            columns_common_letter = 'z'
        return columns_common_letter

    @staticmethod
    def day_6_signals_and_noise_part_1():
        input_file = open('../input.txt', 'r')

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

# ========================= Part 2 ================================== #

    @staticmethod
    def calculate_least_common_letter_of_the_given_column_return_combined_string(
            column_1_list, column_2_list, column_3_list, column_4_list, column_5_list,
            column_6_list, column_7_list, column_8_list):
        column_1_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_1_list)
        column_2_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_2_list)
        column_3_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_3_list)
        column_4_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_4_list)
        column_5_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_5_list)
        column_6_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_6_list)
        column_7_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_7_list)
        column_8_least_common = SignalsAndNoise.calculate_least_common_letter_of_given_list(column_8_list)

        original_string_combined = column_1_least_common + column_2_least_common + column_3_least_common + \
                                   column_4_least_common + column_5_least_common + column_6_least_common + \
                                   column_7_least_common + column_8_least_common

        return original_string_combined

    @staticmethod
    def calculate_least_common_letter_of_given_list(column_list):

        a_least = 0
        b_least = 0
        c_least = 0
        d_least = 0
        e_least = 0
        f_least = 0
        g_least = 0
        h_least = 0
        i_least = 0
        j_least = 0
        k_least = 0
        l_least = 0
        m_least = 0
        n_least = 0
        o_least = 0
        p_least = 0
        q_least = 0
        r_least = 0
        s_least = 0
        t_least = 0
        u_least = 0
        v_least = 0
        w_least = 0
        x_least = 0
        y_least = 0
        z_least = 0

        # sort the list first
        column_list.sort()
        print column_list

        for letter in column_list:
            if letter == 'a':
                a_least += 1
            elif letter == 'b':
                b_least += 1
            elif letter == 'c':
                c_least += 1
            elif letter == 'd':
                d_least += 1
            elif letter == 'e':
                e_least += 1
            elif letter == 'f':
                f_least += 1
            elif letter == 'g':
                g_least += 1
            elif letter == 'h':
                h_least += 1
            elif letter == 'i':
                i_least += 1
            elif letter == 'j':
                j_least += 1
            elif letter == 'k':
                k_least += 1
            elif letter == 'l':
                l_least += 1
            elif letter == 'm':
                m_least += 1
            elif letter == 'n':
                n_least += 1
            elif letter == 'o':
                o_least += 1
            elif letter == 'p':
                p_least += 1
            elif letter == 'q':
                q_least += 1
            elif letter == 'r':
                r_least += 1
            elif letter == 's':
                s_least += 1
            elif letter == 't':
                t_least += 1
            elif letter == 'u':
                u_least += 1
            elif letter == 'v':
                v_least += 1
            elif letter == 'w':
                w_least += 1
            elif letter == 'x':
                x_least += 1
            elif letter == 'y':
                y_least += 1
            elif letter == 'z':
                z_least += 1

        if a_least < b_least and a_least < c_least and a_least < d_least and a_least < e_least and \
            a_least < f_least and a_least < g_least and a_least < h_least and a_least < i_least and \
            a_least < j_least and a_least < k_least and a_least < l_least and a_least < m_least and \
            a_least < n_least and a_least < o_least and a_least < p_least and a_least < q_least and \
            a_least < r_least and a_least < s_least and a_least < t_least and a_least < u_least and \
            a_least < v_least and a_least < w_least and a_least < x_least and a_least < y_least and \
            a_least < z_least:
            columns_least_common_letter = 'a'
        elif b_least < a_least and b_least < c_least and b_least < d_least and b_least < e_least and \
            b_least < f_least and b_least < g_least and b_least < h_least and b_least < i_least and \
            b_least < j_least and b_least < k_least and b_least < l_least and b_least < m_least and \
            b_least < n_least and b_least < o_least and b_least < p_least and b_least < q_least and \
            b_least < r_least and b_least < s_least and b_least < t_least and b_least < u_least and \
            b_least < v_least and b_least < w_least and b_least < x_least and b_least < y_least and \
            b_least < z_least:
            columns_least_common_letter = 'b'
        elif c_least < a_least and c_least < b_least and c_least < d_least and c_least < e_least and \
            c_least < f_least and c_least < g_least and c_least < h_least and c_least < i_least and \
            c_least < j_least and c_least < k_least and c_least < l_least and c_least < m_least and \
            c_least < n_least and c_least < o_least and c_least < p_least and c_least < q_least and \
            c_least < r_least and c_least < s_least and c_least < t_least and c_least < u_least and \
            c_least < v_least and c_least < w_least and c_least < x_least and c_least < y_least and \
            c_least < z_least:
            columns_least_common_letter = 'c'
        elif d_least < a_least and d_least < b_least and d_least < c_least and d_least < e_least and \
            d_least < f_least and d_least < g_least and d_least < h_least and d_least < i_least and \
            d_least < j_least and d_least < k_least and d_least < l_least and d_least < m_least and \
            d_least < n_least and d_least < o_least and d_least < p_least and d_least < q_least and \
            d_least < r_least and d_least < s_least and d_least < t_least and d_least < u_least and \
            d_least < v_least and d_least < w_least and d_least < x_least and d_least < y_least and \
            d_least < z_least:
            columns_least_common_letter = 'd'
        elif e_least < a_least and e_least < b_least and e_least < c_least and e_least < d_least and \
            e_least < f_least and e_least < g_least and e_least < h_least and e_least < i_least and \
            e_least < j_least and e_least < k_least and e_least < l_least and e_least < m_least and \
            e_least < n_least and e_least < o_least and e_least < p_least and e_least < q_least and \
            e_least < r_least and e_least < s_least and e_least < t_least and e_least < u_least and \
            e_least < v_least and e_least < w_least and e_least < x_least and e_least < y_least and \
            e_least < z_least:
            columns_least_common_letter = 'e'
        elif f_least < a_least and f_least < b_least and f_least < c_least and f_least < d_least and \
            f_least < e_least and f_least < g_least and f_least < h_least and f_least < i_least and \
            f_least < j_least and f_least < k_least and f_least < l_least and f_least < m_least and \
            f_least < n_least and f_least < o_least and f_least < p_least and f_least < q_least and \
            f_least < r_least and f_least < s_least and f_least < t_least and f_least < u_least and \
            f_least < v_least and f_least < w_least and f_least < x_least and f_least < y_least and \
            f_least < z_least:
            columns_least_common_letter = 'f'
        elif g_least < a_least and g_least < b_least and g_least < c_least and g_least < d_least and \
            g_least < e_least and g_least < f_least and g_least < h_least and g_least < i_least and \
            g_least < j_least and g_least < k_least and g_least < l_least and g_least < m_least and \
            g_least < n_least and g_least < o_least and g_least < p_least and g_least < q_least and \
            g_least < r_least and g_least < s_least and g_least < t_least and g_least < u_least and \
            g_least < v_least and g_least < w_least and g_least < x_least and g_least < y_least and \
            g_least < z_least:
            columns_least_common_letter = 'g'
        elif h_least < a_least and h_least < b_least and h_least < c_least and h_least < d_least and \
            h_least < e_least and h_least < f_least and h_least < g_least and h_least < i_least and \
            h_least < j_least and h_least < k_least and h_least < l_least and h_least < m_least and \
            h_least < n_least and h_least < o_least and h_least < p_least and h_least < q_least and \
            h_least < r_least and h_least < s_least and h_least < t_least and h_least < u_least and \
            h_least < v_least and h_least < w_least and h_least < x_least and h_least < y_least and \
            h_least < z_least:
            columns_least_common_letter = 'h'
        elif i_least < a_least and i_least < b_least and i_least < c_least and i_least < d_least and \
            i_least < e_least and i_least < f_least and i_least < g_least and i_least < h_least and \
            i_least < j_least and i_least < k_least and i_least < l_least and i_least < m_least and \
            i_least < n_least and i_least < o_least and i_least < p_least and i_least < q_least and \
            i_least < r_least and i_least < s_least and i_least < t_least and i_least < u_least and \
            i_least < v_least and i_least < w_least and i_least < x_least and i_least < y_least and \
            i_least < z_least:
            columns_least_common_letter = 'i'
        elif j_least < a_least and j_least < b_least and j_least < c_least and j_least < d_least and \
            j_least < e_least and j_least < f_least and j_least < g_least and j_least < h_least and \
            j_least < i_least and j_least < k_least and j_least < l_least and j_least < m_least and \
            j_least < n_least and j_least < o_least and j_least < p_least and j_least < q_least and \
            j_least < r_least and j_least < s_least and j_least < t_least and j_least < u_least and \
            j_least < v_least and j_least < w_least and j_least < x_least and j_least < y_least and \
            j_least < z_least:
            columns_least_common_letter = 'j'
        elif k_least < a_least and k_least < b_least and k_least < c_least and k_least < d_least and \
            k_least < e_least and k_least < f_least and k_least < g_least and k_least < h_least and \
            k_least < i_least and k_least < j_least and k_least < l_least and k_least < m_least and \
            k_least < n_least and k_least < o_least and k_least < p_least and k_least < q_least and \
            k_least < r_least and k_least < s_least and k_least < t_least and k_least < u_least and \
            k_least < v_least and k_least < w_least and k_least < x_least and k_least < y_least and \
            k_least < z_least:
            columns_least_common_letter = 'k'
        elif l_least < a_least and l_least < b_least and l_least < c_least and l_least < d_least and \
            l_least < e_least and l_least < f_least and l_least < g_least and l_least < h_least and \
            l_least < i_least and l_least < j_least and l_least < k_least and l_least < m_least and \
            l_least < n_least and l_least < o_least and l_least < p_least and l_least < q_least and \
            l_least < r_least and l_least < s_least and l_least < t_least and l_least < u_least and \
            l_least < v_least and l_least < w_least and l_least < x_least and l_least < y_least and \
            l_least < z_least:
            columns_least_common_letter = 'l'
        elif m_least < a_least and m_least < b_least and m_least < c_least and m_least < d_least and \
            m_least < e_least and m_least < f_least and m_least < g_least and m_least < h_least and \
            m_least < i_least and m_least < j_least and m_least < k_least and m_least < l_least and \
            m_least < n_least and m_least < o_least and m_least < p_least and m_least < q_least and \
            m_least < r_least and m_least < s_least and m_least < t_least and m_least < u_least and \
            m_least < v_least and m_least < w_least and m_least < x_least and m_least < y_least and \
            m_least < z_least:
            columns_least_common_letter = 'm'
        elif n_least < a_least and n_least < b_least and n_least < c_least and n_least < d_least and \
            n_least < e_least and n_least < f_least and n_least < g_least and n_least < h_least and \
            n_least < i_least and n_least < j_least and n_least < k_least and n_least < l_least and \
            n_least < m_least and n_least < o_least and n_least < p_least and n_least < q_least and \
            n_least < r_least and n_least < s_least and n_least < t_least and n_least < u_least and \
            n_least < v_least and n_least < w_least and n_least < x_least and n_least < y_least and \
            n_least < z_least:
            columns_least_common_letter = 'n'
        elif o_least < a_least and o_least < b_least and o_least < c_least and o_least < d_least and \
            o_least < e_least and o_least < f_least and o_least < g_least and o_least < h_least and \
            o_least < i_least and o_least < j_least and o_least < k_least and o_least < l_least and \
            o_least < m_least and o_least < n_least and o_least < p_least and o_least < q_least and \
            o_least < r_least and o_least < s_least and o_least < t_least and o_least < u_least and \
            o_least < v_least and o_least < w_least and o_least < x_least and o_least < y_least and \
            o_least < z_least:
            columns_least_common_letter = 'o'
        elif p_least < a_least and p_least < b_least and p_least < c_least and p_least < d_least and \
            p_least < e_least and p_least < f_least and p_least < g_least and p_least < h_least and \
            p_least < i_least and p_least < j_least and p_least < k_least and p_least < l_least and \
            p_least < m_least and p_least < n_least and p_least < o_least and p_least < q_least and \
            p_least < r_least and p_least < s_least and p_least < t_least and p_least < u_least and \
            p_least < v_least and p_least < w_least and p_least < x_least and p_least < y_least and \
            p_least < z_least:
            columns_least_common_letter = 'p'
        elif q_least < a_least and q_least < b_least and q_least < c_least and q_least < d_least and \
            q_least < e_least and q_least < f_least and q_least < g_least and q_least < h_least and \
            q_least < i_least and q_least < j_least and q_least < k_least and q_least < l_least and \
            q_least < m_least and q_least < n_least and q_least < o_least and q_least < p_least and \
            q_least < r_least and q_least < s_least and q_least < t_least and q_least < u_least and \
            q_least < v_least and q_least < w_least and q_least < x_least and q_least < y_least and \
            q_least < z_least:
            columns_least_common_letter = 'q'
        elif r_least < a_least and r_least < b_least and r_least < c_least and r_least < d_least and \
            r_least < e_least and r_least < f_least and r_least < g_least and r_least < h_least and \
            r_least < i_least and r_least < j_least and r_least < k_least and r_least < l_least and \
            r_least < m_least and r_least < n_least and r_least < o_least and r_least < p_least and \
            r_least < q_least and r_least < s_least and r_least < t_least and r_least < u_least and \
            r_least < v_least and r_least < w_least and r_least < x_least and r_least < y_least and \
            r_least < z_least:
            columns_least_common_letter = 'r'
        elif s_least < a_least and s_least < b_least and s_least < c_least and s_least < d_least and \
            s_least < e_least and s_least < f_least and s_least < g_least and s_least < h_least and \
            s_least < i_least and s_least < j_least and s_least < k_least and s_least < l_least and \
            s_least < m_least and s_least < n_least and s_least < o_least and s_least < p_least and \
            s_least < q_least and s_least < r_least and s_least < t_least and s_least < u_least and \
            s_least < v_least and s_least < w_least and s_least < x_least and s_least < y_least and \
            s_least < z_least:
            columns_least_common_letter = 's'
        elif t_least < a_least and t_least < b_least and t_least < c_least and t_least < d_least and \
            t_least < e_least and t_least < f_least and t_least < g_least and t_least < h_least and \
            t_least < i_least and t_least < j_least and t_least < k_least and t_least < l_least and \
            t_least < m_least and t_least < n_least and t_least < o_least and t_least < p_least and \
            t_least < q_least and t_least < r_least and t_least < s_least and t_least < u_least and \
            t_least < v_least and t_least < w_least and t_least < x_least and t_least < y_least and \
            t_least < z_least:
            columns_least_common_letter = 't'
        elif u_least < a_least and u_least < b_least and u_least < c_least and u_least < d_least and \
            u_least < e_least and u_least < f_least and u_least < g_least and u_least < h_least and \
            u_least < i_least and u_least < j_least and u_least < k_least and u_least < l_least and \
            u_least < m_least and u_least < n_least and u_least < o_least and u_least < p_least and \
            u_least < q_least and u_least < r_least and u_least < s_least and u_least < t_least and \
            u_least < v_least and u_least < w_least and u_least < x_least and u_least < y_least and \
            u_least < z_least:
            columns_least_common_letter = 'u'
        elif v_least < a_least and v_least < b_least and v_least < c_least and v_least < d_least and \
            v_least < e_least and v_least < f_least and v_least < g_least and v_least < h_least and \
            v_least < i_least and v_least < j_least and v_least < k_least and v_least < l_least and \
            v_least < m_least and v_least < n_least and v_least < o_least and v_least < p_least and \
            v_least < q_least and v_least < r_least and v_least < s_least and v_least < t_least and \
            v_least < u_least and v_least < w_least and v_least < x_least and v_least < y_least and \
            v_least < z_least:
            columns_least_common_letter = 'v'
        elif w_least < a_least and w_least < b_least and w_least < c_least and w_least < d_least and \
            w_least < e_least and w_least < f_least and w_least < g_least and w_least < h_least and \
            w_least < i_least and w_least < j_least and w_least < k_least and w_least < l_least and \
            w_least < m_least and w_least < n_least and w_least < o_least and w_least < p_least and \
            w_least < q_least and w_least < r_least and w_least < s_least and w_least < t_least and \
            w_least < u_least and w_least < v_least and w_least < x_least and w_least < y_least and \
            w_least < z_least:
            columns_least_common_letter = 'w'
        elif x_least < a_least and x_least < b_least and x_least < c_least and x_least < d_least and \
            x_least < e_least and x_least < f_least and x_least < g_least and x_least < h_least and \
            x_least < i_least and x_least < j_least and x_least < k_least and x_least < l_least and \
            x_least < m_least and x_least < n_least and x_least < o_least and x_least < p_least and \
            x_least < q_least and x_least < r_least and x_least < s_least and x_least < t_least and \
            x_least < u_least and x_least < v_least and x_least < w_least and x_least < y_least and \
            x_least < z_least:
            columns_least_common_letter = 'x'
        elif y_least < a_least and y_least < b_least and y_least < c_least and y_least < d_least and \
            y_least < e_least and y_least < f_least and y_least < g_least and y_least < h_least and \
            y_least < i_least and y_least < j_least and y_least < k_least and y_least < l_least and \
            y_least < m_least and y_least < n_least and y_least < o_least and y_least < p_least and \
            y_least < q_least and y_least < r_least and y_least < s_least and y_least < t_least and \
            y_least < u_least and y_least < v_least and y_least < w_least and y_least < x_least and \
            y_least < z_least:
            columns_least_common_letter = 'y'
        else:
            columns_least_common_letter = 'z'
        return columns_least_common_letter

    @staticmethod
    def day_6_signals_and_noise_part_2():
        input_file = open('../input.txt', 'r')

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
        day_6_part_2_answer = SignalsAndNoise. \
            calculate_least_common_letter_of_the_given_column_return_combined_string(column_1_list,
                                                                              column_2_list,
                                                                              column_3_list,
                                                                              column_4_list,
                                                                              column_5_list,
                                                                              column_6_list,
                                                                              column_7_list,
                                                                              column_8_list)
        print "Day 6 Part 2 Answer: " + day_6_part_2_answer
        return day_6_part_2_answer
