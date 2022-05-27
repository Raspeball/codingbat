## https://codingbat.com/python/String-1 ##
# all string-1 problems in one file #
#
#
#
# hello_name #
'''Given a string name, e.g. "Bob",
return a greeting of the form "Hello Bob!".'''

def hello_name(name):
    return "Hello " + name + "!"
#
#
#
# make_abba #
'''Given two strings, a and b, return the result of putting them together in the
order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".'''

def make_abba(a, b):
    res = a + 2*b + a
    return res
#
#
#
# make_tags #
'''The web is built with HTML strings like "<i>Yay</i>" which
draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which
surround the word "Yay". Given tag and word strings, create the HTML string
with tags around the word, e.g. "<i>Yay</i>".'''

def make_tags(tag, word):
    tagged = "<{}>{}</{}>".format(tag, word, tag)
    return tagged
#
#
#
# make_out_word #
'''Given an "out" string length 4, such as "<<>>", and a word, return a new
string where the word is in the middle of the out string, e.g. "<<word>>".'''

def make_out_word(out, word):
    res = "{}{}{}".format(out[0:2], word, out[2:4])
    return res
#
#
#
# extra_end #
''' Given a string, return a new string made of 3 copies of the last 2 chars of
the original string. The string length will be at least 2.'''

def extra_end(string):
    new = 3*string[-2:]
    return new
