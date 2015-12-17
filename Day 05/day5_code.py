__author__ = 'smelnyk'


def find_number_strings_that_are_nice(strings):
    """
    Santa needs help figuring out which strings in his text file are naughty or nice.

    A nice string is one with all of the following properties:

    * It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    * It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or
      aabbccdd (aa, bb, cc, or dd).
    * It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the
      other requirements.

    :param strings: a list of strings to check against
    :return: num of strings matching the "nice" criteria
    """

    num_of_vowels = 0
    num_of_nice_strings = 0

    # loop over each character in the string
    for character in strings:
        # if three vowels found (aeiou)
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            # incrememt num_of_vowels to be 1
            num_of_vowels += 1

    # If the string has at least three vowels
    if num_of_vowels >= 3:
        num_of_nice_strings += 1

    # check if the string contains at least one letter that appears twice in a row, like xx, abcdde (dd), or
    # aabbccdd (aa, bb, cc, or dd).

    # check that it doesn't contain the following strings(ab, cd, pq, or xy)
    # even if they are part of one of the other requirements.

    if num_of_vowels >= 3:
        num_of_nice_strings += 1

    # return num_of_nice_words
    print "num_of_nice_strings is: " + str(num_of_nice_strings)
    return num_of_nice_strings