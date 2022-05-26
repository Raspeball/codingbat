## https://codingbat.com/prob/p182414 ##
# string_match #

'''
Given 2 strings, a and b, return the number of the positions where they contain
the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
appear in the same place in both strings.'''

def string_match(a, b):
    n = 0

    if len(b) < 2 or len(b) < 2:
        n = 0

    else:
        sub2_a = [a[i: i+2] for i in range(len(a)-1)]
        sub2_b = [b[i: i+2] for i in range(len(b)-1)]

        shortest = min(len(a), len(b))

        for i in range(shortest - 1): # len(a) - 1 = len(sub2_a)
            if sub2_a[i] == sub2_b[i]:
                n += 1
            else: continue

    return n

test = string_match("abcd", "abcdefghi")
