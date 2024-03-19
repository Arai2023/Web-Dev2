def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)
    remaining = goal - max_big * 5
    if remaining <= small:
        return remaining
    return -1

# Test cases
print(make_chocolate(4, 1, 9))  # 4
print(make_chocolate(4, 1, 10)) # -1
print(make_chocolate(4, 1, 7))  # 2
