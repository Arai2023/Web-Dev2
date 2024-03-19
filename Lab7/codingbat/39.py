def max_end3(nums):
    max_num = max(nums[0], nums[2])
    return [max_num] * 3

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))
