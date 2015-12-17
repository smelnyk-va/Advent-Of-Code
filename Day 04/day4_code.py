__author__ = 'smelnyk'

import md5

"""
Santa needs help mining some AdventCoins (very similar to bitcoins) to use
as gifts for all the economically forward-thinking little girls and boys.

* To do this, he needs to find MD5 hashes which, in hexadecimal, start with
  at least five zeroes.

* The input to the MD5 hash is some secret key (your puzzle input, given
  below) followed by a number in decimal.

* To mine AdventCoins, you must find Santa the lowest positive number
  (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
such number to do so.

If your secret key is pqrstuv, the lowest number it combines with to make an
MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
pqrstuv1048970 looks like 000006136ef....

Your puzzle input is: yzbqklnj
"""


def mine_bitcoins(secret_key):

    print "secret_key is: " + str(secret_key)

    hash_answer = ''
    hash_hexdigest = ''

    secret_key_updated = ''

    md5_hash = md5.new()

    # Time to find the lowest number the hex combines with to make a MD5
    # hash starting with five zeros
    # Keep regenerating the hash until we get one with 5 leading zeros
        # return the number that produced a has with the 5 leading zeros?

    for x in range(0, 1048971):

        # Need to append the number at the end of the string and then update that, not 2 updates
        secret_key_updated = secret_key + str(x)
        # print "secret_key_updated is: " + str(secret_key_updated)

        md5_hash.update(secret_key_updated)

        # print "md5_hash is: " + str(md5_hash)

        hash_hexdigest = md5_hash.hexdigest()
        hash_answer = hash_hexdigest

        # print "Current hash_answer is: " + str(hash_answer)

        if hash_answer.startswith('00000'):
            print "Current hash_answer is: " + str(hash_answer)
            return x

