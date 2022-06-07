## https://codingbat.com/prob/p149391 ##
# xyz_there #

'''Return True if the given string contains an appearance of "xyz"
where the xyz is not directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not.'''

def xyz_there(string):
    is_xyz = False
    for i in range(len(string) - 2):
        if string[i: i + 3].lower() == "xyz" and string[i-1] != ".":
            is_xyz = True

    return is_xyz
