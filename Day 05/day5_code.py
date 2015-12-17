__author__ = 'smelnyk'

"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

* It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
* It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or
  aabbccdd (aa, bb, cc, or dd).
* It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the
  other requirements.
"""


def get_total_of_nice_strings(strings):

    num_of_nice_strings = 0

    for string in strings:
        print "string is: " + str(string)
        # string.replace('\n', '')
        num_of_nice_strings += determine_if_string_has_three_vowels(string)
        num_of_nice_strings += determine_if_at_least_one_letter_appears_twice_in_a_row_in_string(string)
        num_of_nice_strings += determine_if_string_has_ab_cd_pq_or_xy(string)

    print "The Total of Nice Strings is: " + str(num_of_nice_strings)
    return num_of_nice_strings


def determine_if_string_has_three_vowels(string):
    # check if string contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    num_of_vowels = 0
    num_of_nice_strings = 0

    # loop over each character in the string
    for character in string:
        # if current character is a vowel (aeiou)
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            # incrememt num_of_vowels to be 1
            num_of_vowels += 1

    # If the string has at least three vowels
    if num_of_vowels >= 3:
        # the string passes the first check
        num_of_nice_strings += 1

    print "num_of_nice_strings is (determine_if_string_has_three_vowels): " + str(num_of_nice_strings)
    print
    return num_of_nice_strings


def determine_if_at_least_one_letter_appears_twice_in_a_row_in_string(string):
    # check if the string contains at least one letter that appears twice in a row, like xx, abcdde
    # (dd), or aabbccdd (aa, bb, cc, or dd).

    num_of_nice_strings = 0



    print "num_of_nice_strings (determine_if_letter_appears_twice_in_a_row_in_string is): " + str(num_of_nice_strings)
    print
    return num_of_nice_strings


def determine_if_string_has_ab_cd_pq_or_xy(string):
    # check that it doesn't contain the following strings(ab, cd, pq, or xy)
    # even if they are part of one of the other requirements.
    print "string is (determine_if_string_has_ab_cd_pq_or_xy): " + str(string)

    num_of_nice_strings = 0
    has_ab = 0
    has_cd = 0
    has_pq = 0
    has_xy = 0

    # Need a way to loop over the current string to do each check just once for each string passed in

    has_ab = string.find('ab')
    print "has_ab is: " + str(has_ab)

    has_cd = string.find('cd')
    print "has_cd is: " + str(has_cd)

    has_pq = string.find('pq')
    print "has_pq is: " + str(has_pq)

    has_xy = string.find('xy')
    print "has_xy is: " + str(has_xy)

    # If string does not have "ab", "cd', "pg" or "xy"
    if has_ab == -1 and has_cd == -1 and has_pq == -1 and has_xy == -1:
        # the string passes the rule
        num_of_nice_strings += 1

    print "num_of_nice_strings (determine_if_string_has_ab_cd_pq_or_xy is): " + str(num_of_nice_strings)
    print
    return num_of_nice_strings


