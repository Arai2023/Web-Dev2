def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1
    return total

# Test cases
print(sum13([1, 2, 2, 1]))         # 6
print(sum13([1, 1]))                # 2
print(sum13([1, 2, 2, 1, 13]))      # 6
