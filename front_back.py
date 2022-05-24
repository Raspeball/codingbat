## https://codingbat.com/prob/p153599 ##
# front_back #

'''
Given a string,
return a new string where the first and last chars have been exchanged.'''

def front_back(str):
    ln = len(str)

    if ln <= 1:
        return str
    else:
        return str[-1] + str[1:ln-1] + str[0]
