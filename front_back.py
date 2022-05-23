## https://codingbat.com/prob/p153599 ##

def front_back(str):
    ln = len(str)

    if ln <= 1:
        return str
    else:
        return str[-1] + str[1:ln-1] + str[0]
