## https://codingbat.com/prob/p166884 ##
# parrot_trouble #

'''
We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.'''


def parrot_trouble(talking, hour):

    if talking and (hour > 20 or hour < 7):
        return True

    else: return False
