## https://codingbat.com/prob/p118366 ##
# string_splosion #

'''Given a non-empty string like "Code" return a string like "CCoCodCode".'''

def string_splosion(string):
    res = ""

    for ind, val in enumerate(string):
        res = res + string[:ind+1]

    return res

print(string_splosion("Code"))
