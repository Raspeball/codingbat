## https://codingbat.com/prob/p174314 ##
# end_other #

'''Given two strings, return True if either of the strings appears at the very
end of the other string, ignoring upper/lower case differences
(in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.'''


def end_other(a, b):
    is_end = False

    if a.lower() == b[len(b) - len(a):].lower():
        is_end = True

    elif b.lower() == a[len(a) - len(b):].lower():
        is_end = True

    return is_end

# codingbat solution #
#def end_other(a, b):
#   a = a.lower()
#   b = b.lower()
#   return (b.endswith(a) or a.endswith(b))
