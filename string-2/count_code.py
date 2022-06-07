def count_code(string):
    count_code = 0
    for i in range(len(string)- 3):
        if string[i:i+2].lower() == "co" and string[i+3].lower() == "e":
            count_code += 1
    
    return count_code

test = count_code("codexxcode")
print(test)
        