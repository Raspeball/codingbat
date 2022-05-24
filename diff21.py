## https://codingbat.com/prob/p197466 ##
# diff21 #

'''Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.'''

def diff21(n):
    val = abs(n-21)

    if n > 21:
        val = val*2

    return val
