## https://codingbat.com/prob/p141905 ##
# sum_double #

'''Given two int values, return their sum. Unless the two values are the same,
then return double their sum.'''

def sum_double(a, b):

    if a == b:
        return 2*(a+b)

    else:
        return a + b


def sum_double_lf(a, b):

    s = a + b

    if a == b:
        s = s*2

    return s
