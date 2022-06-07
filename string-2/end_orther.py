def end_other(a, b):
    is_end = False
    
    if a.lower() == b[len(b) - len(a):].lower():
        is_end = True
    
    elif b.lower() == a[len(a) - len(b):].lower():
        is_end = True
    
    return is_end

test = end_other('abc', 'abXabc')

print(test)