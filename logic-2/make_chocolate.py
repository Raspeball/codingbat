## https://codingbat.com/prob/p190859 ##
# make_chocolate #

'''
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use,
assuming we always use big bars before small bars.
Return -1 if it can't be done.'''

def make_chocolate(small, big, goal):

    res = goal

    if goal // big < 5:
        res = goal % 5

    else:
        res = res - big*5

    if res > small:
        res = -1

    return res
