def has22(nums):
    # Iterate through the list
    for i in range(len(nums) - 1):
        # Check if current and next elements are both 2
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

# Test cases
print(has22([1, 2, 2]))  # True
print(has22([1, 2, 1, 2]))  # False
print(has22([2, 1, 2]))  # False
