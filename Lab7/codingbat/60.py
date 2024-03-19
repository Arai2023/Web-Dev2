def close_far(a, b, c):
    if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    elif abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False

# Test cases
print(close_far(1, 2, 10))  # True
print(close_far(1, 2, 3))    # False
print(close_far(4, 1, 3))    # True
