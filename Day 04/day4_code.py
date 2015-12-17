__author__ = 'smelnyk'

import md5


def mine_bitcoins_part1(secret_key):
    """
    Santa needs help mining some AdventCoins (very similar to bitcoins) to use
    as gifts for all the economically forward-thinking little girls and boys.

    * To do this, he needs to find MD5 hashes which, in hexadecimal, starts with
      at least five zeroes.

    * The input to the MD5 hash is some secret key (your puzzle input, given
      below) followed by a number in decimal.

    * To mine AdventCoins, you must find Santa the lowest positive number
      (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
    """

    # print "secret_key is: " + str(secret_key)

    hash_answer = ''
    hash_hexdigest = ''
    secret_key_updated = ''

    for x in range(0, 1048971):

        secret_key_updated = secret_key + str(x)
        # print "secret_key_updated is: " + str(secret_key_updated)

        md5_hash = md5.new()
        md5_hash.update(secret_key_updated)
        hash_hexdigest = md5_hash.hexdigest()
        hash_answer = hash_hexdigest
        # print "Current hash_answer is: " + str(hash_answer)

        if hash_answer.startswith('00000'):
            print "Current hash_answer is: " + str(hash_answer)
            return x


def mine_bitcoins_part2(secret_key):
    """
    Santa needs help mining some AdventCoins (very similar to bitcoins) to use
    as gifts for all the economically forward-thinking little girls and boys.

    * To do this, he needs to find MD5 hashes which, in hexadecimal, starts with
      at least six zeroes.

    * The input to the MD5 hash is some secret key (your puzzle input, given
      below) followed by a number in decimal.

    * To mine AdventCoins, you must find Santa the lowest positive number
      (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
    """

    # print "secret_key is: " + str(secret_key)

    hash_answer = ''
    hash_hexdigest = ''
    secret_key_updated = ''

    for x in range(0, 10000000):

        secret_key_updated = secret_key + str(x)
        # print "secret_key_updated is: " + str(secret_key_updated)

        md5_hash = md5.new()
        md5_hash.update(secret_key_updated)
        hash_hexdigest = md5_hash.hexdigest()
        hash_answer = hash_hexdigest
        # print "Current hash_answer is: " + str(hash_answer)

        if hash_answer.startswith('000000'):
            print "Current hash_answer is: " + str(hash_answer)
            return x

