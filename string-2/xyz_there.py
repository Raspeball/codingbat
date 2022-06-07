def xyz_there(string):
    is_xyz = False
    for i in range(len(string) - 2):
        if string[i: i + 3].lower() == "xyz" and string[i-1] != ".":
            is_xyz = True
    
    return is_xyz