## https://codingbat.com/prob/p145834 ##
# last2 #


'''Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).'''

def last2(string):
    n = 0
    sub = string[len(string) - 2: len(string)]

    if len(string) < 2:
        n = 0

    else:
        for i in range(len(string) - 1):
            if string[i: i+2] == sub:
                n += 1
            else:
                continue
        n = n - 1

    return n
