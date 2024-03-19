def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

# Test cases
print(love6(6, 4))  # True
print(love6(4, 5))  # False
print(love6(1, 5))  # True
