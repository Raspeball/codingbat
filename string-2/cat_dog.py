## https://codingbat.com/prob/p164876 ##
# cat_dog #

'''Return True if the string "cat" and "dog" appear the same number of times
in the given string.'''

def cat_dog(string):

    lows = string.lower()

    return lows.count("cat") == lows.count("dog")
