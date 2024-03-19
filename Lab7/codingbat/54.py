def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small

# Test cases
print(make_bricks(3, 1, 8)) # True
print(make_bricks(3, 1, 9)) # False
print(make_bricks(3, 2, 10)) # True
