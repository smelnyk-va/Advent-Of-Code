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
    num_of_copies_of_number = 0

    if input_number == 1:

        single_digit_1 = 1

        num_of_copies_of_number += input_number
        print "num_of_copies_of_number is: " + str(num_of_copies_of_number)

        new_number = str(num_of_copies_of_number) + str(single_digit_1)
        print "new_number is: " + str(new_number)

    if input_number == 11:

        single_digit_1 = 1

        num_of_copies_of_number = (input_number + input_number) / input_number
        print "num_of_copies_of_number is: " + str(num_of_copies_of_number)

        new_number = str(num_of_copies_of_number) + str(single_digit_1)
        print "new_number is: " + str(new_number)

    if input_number == 21:

        single_digit_1 = 2
        single_digit_2 = 1

        if single_digit_1 == single_digit_2:
            num_of_copies_of_number = (input_number + input_number) / input_number
            print "num_of_copies_of_number is: " + str(num_of_copies_of_number)
        else:
            num_of_copies_of_number += 1
            print "num_of_copies_of_number is: " + str(num_of_copies_of_number)

        new_number = str(single_digit_2) + str(single_digit_1) + str(num_of_copies_of_number) + str(single_digit_2)
        print "new_number is: " + str(new_number)

    print
    return int(new_number)



