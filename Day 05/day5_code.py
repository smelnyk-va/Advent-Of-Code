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

def one_funtion_to_do_it_all(strings):

    # print "strings is: " + str(strings.read())

    num_of_nice_strings = 0
    has_ab = 0
    has_cd = 0
    has_pq = 0
    has_xy = 0
    num_of_vowels_in_string = 0

    passed_vowel_test = False
    passed_repeated_character_test = False
    passed_third_test = False

    # Loop through all the individual strings in the list of strings
    for string in strings:
        print "string is: " + str(string)

        string = string.replace('\n', '')
        num_of_vowels_in_string = 0

        # ==== Check if String Passes the First Rule check ==== #
        # loop over each character in the string
        for character in string:
            # if current character is a vowel (aeiou)
            if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
                # increment num_of_vowels_in_string by 1
                num_of_vowels_in_string += 1

        # If the string has at least three vowels
        if num_of_vowels_in_string >= 3:
            # the String passes the First rule check
            passed_vowel_test = True

        # ==== Check if String Passes the Second Rule check ==== #
        # loop through each character in the string until we get to the end of the string
        for character in range(len(string)-1):
            # if the current character matches the character next to it
            if string[character+1] == string[character]:
                # the String passes the second rule check
                passed_repeated_character_test = True

        # ==== Check if String Passes the Third Rule check ==== #
        has_ab = string.find('ab')
        # print "has_ab is: " + str(has_ab)
        has_cd = string.find('cd')
        # print "has_cd is: " + str(has_cd)
        has_pq = string.find('pq')
        # print "has_pq is: " + str(has_pq)
        has_xy = string.find('xy')
        # print "has_xy is: " + str(has_xy)

        # If string does not have "ab", "cd', "pg" or "xy"
        if has_ab == -1 and has_cd == -1 and has_pq == -1 and has_xy == -1:
            # the String passes the third rule check
            passed_third_test = True

        # ==== Check if String Passes the All Three Rule checks ==== #
        if passed_vowel_test and passed_repeated_character_test and passed_third_test:
            # this string is a "Nice" word
            num_of_nice_strings += 1

            # reset the checks for the new word
            passed_vowel_test = False
            passed_repeated_character_test = False
            passed_third_test = False
        else:
            # reset the checks for the new word
            passed_vowel_test = False
            passed_repeated_character_test = False
            passed_third_test = False

    return num_of_nice_strings


# ==== The separate functions below aren't needed once the above is working ==== #
"""
I broke it out into separate methods to get the code working first and then combined them to all be in the
same function above.

Another way to redo this day would be using regexes.
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

    # print "string is: " + str(string)

    num_of_nice_strings = 0
    repeated_character_exists = False

    # loop through each character in the string until we get to the end of the string
    for character in range(len(string)-1):

        # if the current character matches the character next to it
        if string[character+1] == string[character]:
            # It matches the rule
            repeated_character_exists = True

            if repeated_character_exists:
                num_of_nice_strings += 1
                return num_of_nice_strings

    # print "num_of_nice_strings (determine_if_letter_appears_twice_in_a_row_in_string is): " + str(num_of_nice_strings)
    # print
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


