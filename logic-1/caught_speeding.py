## https://codingbat.com/prob/p137202 ##
# caught_speeding #

'''You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small
ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is
between 61 and 80 inclusive, the result is 1. If speed is 81 or more,
the result is 2. Unless it is your birthday -- on that day, your speed can be
5 higher in all cases.'''

# this produces correct results for all codingbat runs
# but codingbat does not agree
def caught_speeding(speed, is_birthday):
    ticket = 1
    low, high = 61, 81

    if is_birthday:
        speed = speed - 5

    if speed not in range(low, high):
        ticket += int(((speed - low)/high) - 1) + 1

    return ticket

# DV solution
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed -5

    return (speed > 60) + (speed > 80)
