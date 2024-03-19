def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    else:
        return a + b

# Test cases
print(sorta_sum(3, 4))    # 7
print(sorta_sum(9, 4))    # 20
print(sorta_sum(10, 11))  # 21
