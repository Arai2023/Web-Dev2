def xyz_there(string):
    for i in range(len(string) - 2):
        if string[i:i+3] == 'xyz' and (i == 0 or string[i-1] != '.'):
            return True
    return False

# Test cases
print(xyz_there('abcxyz'))   # True
print(xyz_there('abc.xyz'))  # False
print(xyz_there('xyz.abc'))  # True
