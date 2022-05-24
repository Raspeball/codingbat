## https://codingbat.com/prob/p147920 ##
# front3 #

'''Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there.
Return a new string which is 3 copies of the front.'''

def front3(string):
    front = ""
    if len(string) < 3:
        front = string*3
    else:
        for i in range(3):
            front += string[i]
        front = front*3

    return front

test = front3("abc")
print(test)
