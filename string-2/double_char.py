def double_char(string):
    double = ""
    for char in string:
        double += 2*char
    
    return double

x = double_char("The")
print(x)