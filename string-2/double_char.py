## https://codingbat.com/prob/p170842 ##
# double_char #

'''Given a string, return a string where for every char in the original,
there are two chars.'''


def double_char(string):
    double = ""
    for char in string:
        double += 2*char

    return double
