__author__ = 'smelnyk'

"""
Today, the Elves are playing a game called look-and-say.
They take turns making sequences by reading aloud the previous sequence and
using that reading as the next sequence.

For example:
211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value
as input for the next step.

For each step, take the previous value, and replace each run of digits
(like 111) with the number of digits (3) followed by the digit itself (1).

For example:
1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times.
What is the length of the result?
"""


def get_total_length(input_number):

    print "input_number is: " + str(input_number)

    new_number = ""
    copy_of_number_one = 0
    copy_of_number_two = 0
    copy_of_number_three = 0
    copy_of_number_four = 0
    copy_of_number_five = 0
    copy_of_number_six = 0
    copy_of_number_seven = 0
    copy_of_number_eight = 0
    copy_of_number_nine = 0
    copy_of_number_zero = 0

    # Make int into a string so it's iterable
    string_of_input_numbers = str(input_number)

    len_of_input_numbers = len(string_of_input_numbers)
    print "len_of_input_numbers is: " + str(len_of_input_numbers)

    if len_of_input_numbers >= 1:
        for number in string_of_input_numbers:
            print "number is: " + number
            if number == '1':
                string_value = '1'
                copy_of_number_one += 1
                new_number += str(copy_of_number_one) + string_value

            elif number == '2':
                string_value = '2'
                copy_of_number_two += 1
                new_number += str(copy_of_number_two) + string_value

            elif number == '3':
                string_value = '3'
                copy_of_number_three += 1
                new_number += str(copy_of_number_three) + string_value

            elif number == '4':
                string_value = '4'
                copy_of_number_four += 1
                new_number += str(copy_of_number_four) + string_value

            elif number == '5':
                string_value = '5'
                copy_of_number_five += 1
                new_number += str(copy_of_number_five) + string_value

            elif number == '6':
                string_value = '6'
                copy_of_number_six += 1
                new_number += str(copy_of_number_six) + string_value

            elif number == '7':
                string_value = '7'
                copy_of_number_seven += 1
                new_number += str(copy_of_number_seven) + string_value

            elif number == '8':
                string_value = '8'
                copy_of_number_eight += 1
                new_number += str(copy_of_number_eight) + string_value

            elif number == '9':
                string_value = '9'
                copy_of_number_nine += 1
                new_number += str(copy_of_number_nine) + string_value

            else:
                string_value = '0'
                copy_of_number_zero += 1
                new_number += str(copy_of_number_zero) + string_value

    print "new_number is: " + str(new_number)
    print
    return int(new_number)



