def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b
    else:
        return a + b + c

# Test cases
print(lone_sum(1, 2, 3)) # 6
print(lone_sum(3, 2, 3)) # 2
print(lone_sum(3, 3, 3)) # 0
