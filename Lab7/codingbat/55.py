def fix_teen(n):
    return 0 if 13 <= n <= 19 and n != 15 and n != 16 else n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

# Test cases
print(no_teen_sum(1, 2, 3)) # 6
print(no_teen_sum(2, 13, 1)) # 3
print(no_teen_sum(2, 1, 14)) # 3
