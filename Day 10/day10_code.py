__author__ = 'smelnyk'

# from itertools import groupby
import re

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

    # The way I have this programmed right now will not work.
    # I need it to basically:
    # Will need a loop within a loop?
        # Grab the input value (the look number)
        # determine the say value and check value
        # create string accordingly
        # re-pass new value through the loop
        # re-create the string accordingly
        # return the len of the final number after looping through 40 times.

    # for loop_times in range(40): # Need to a way to make it loop through this 40 times. This doesn't work.
    for number in string_of_input_numbers:
        print "number is: " + number
        if number == '1':
            copy_of_number_one += 1
            new_number += str(copy_of_number_one) + number

        elif number == '2':
            copy_of_number_two += 1
            new_number += str(copy_of_number_two) + number

        elif number == '3':
            copy_of_number_three += 1
            new_number += str(copy_of_number_three) + number

        elif number == '4':
            copy_of_number_four += 1
            new_number += str(copy_of_number_four) + number

        elif number == '5':
            copy_of_number_five += 1
            new_number += str(copy_of_number_five) + number

        elif number == '6':
            copy_of_number_six += 1
            new_number += str(copy_of_number_six) + number

        elif number == '7':
            copy_of_number_seven += 1
            new_number += str(copy_of_number_seven) + number

        elif number == '8':
            copy_of_number_eight += 1
            new_number += str(copy_of_number_eight) + number

        elif number == '9':
            copy_of_number_nine += 1
            new_number += str(copy_of_number_nine) + number
        else:
            copy_of_number_zero += 1
            new_number += str(copy_of_number_zero) + number

    # if loop_times == 40:
    # Note, need to return the length of the new number.
    int_new_num = int(new_number)
    print "int_new_num is: " + str(int_new_num)
    len_of_new_num = len(new_number)  # Once code appears to be working, use this answer
    print "len_of_new_num is: " + str(len_of_new_num)
    print
    return int_new_num


# ===================================================================================== #

# This is Chris Penner's Solution
# He's properly looping through 40 times here.
def look_and_say_chris_part1(input_string):
    current_input = input_string
    # This is a little complicated, we find a digit and capture all of its
    # repetitions, in the second capture group we have the single digit itself
    repeating_digits = re.compile(r'((\d)\2*)')

    for i in range(0, 40):
        new_input = ''
        # Unpack into the total match and the single digit.
        for match, character in repeating_digits.findall(current_input):
            new_input += str(len(match))
            new_input += character
        current_input = new_input

    # Need to return the length of the input, not the value of the input
    return str(len(current_input))


def look_and_say_chris_part2(input_string):
    current_input = input_string
    # This is a little complicated, we find a digit and capture all of its
    # repetitions, in the second capture group we have the single digit itself
    repeating_digits = re.compile(r'((\d)\2*)')

    for i in range(0, 50):
        new_input = ''
        # Unpack into the total match and the single digit.
        for match, character in repeating_digits.findall(current_input):
            new_input += str(len(match))
            new_input += character
        current_input = new_input

    # Need to return the length of the input, not the value of the input
    return str(len(current_input))
