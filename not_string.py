## https://codingbat.com/prob/p189441 ##

def not_string(str):
    parts = str.split()

    if parts[0].lower() == "not":
        return str

    else:
        return "not " + str
