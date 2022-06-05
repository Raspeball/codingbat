## https://codingbat.com/prob/p116620 ##
# sorta_sum #

'''Given 2 ints, a and b, return their sum.
However, sums in the range 10..19 inclusive, are forbidden,
so in that case just return 20.'''

def sorta_sum(a, b):
    s = a + b
    if s in range(10, 20):
        s = 20

    return s
