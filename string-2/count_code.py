## https://codingbat.com/prob/p186048 ##
# count_code #

'''Return the number of times that the string "code" appears anywhere in the
given string, except we'll accept any letter for the 'd',
so "cope" and "cooe" count.'''

def count_code(string):
    count_code = 0
    for i in range(len(string)- 3):
        if string[i:i+2].lower() == "co" and string[i+3].lower() == "e":
            count_code += 1

    return count_code
