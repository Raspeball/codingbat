## https://codingbat.com/prob/p160533 ##
# close_far #

'''Given three ints, a b c, return True if one of b or c is "close"
(differing from a by at most 1), while the other is "far",
differing from both other values by 2 or more.
Note: abs(num) computes the absolute value of a number.'''

def close_far(a, b, c):
    far = 2

    if abs(a - b) < far:
        return abs(a - c) >= far and abs(b - c) >= far

    elif abs(a - c) < far:
        return abs(a - b) >= far and abs(b - c) >= far

    else:
        return False
