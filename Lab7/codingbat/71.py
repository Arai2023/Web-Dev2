def centered_average(nums):
    # Remove the largest and smallest values
    nums.remove(max(nums))
    nums.remove(min(nums))
    
    # Calculate the sum of remaining elements
    total = sum(nums)
    
    # Calculate the average
    avg = total // len(nums)
    
    return avg

# Test cases
print(centered_average([1, 2, 3, 4, 100]))  # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # 5
print(centered_average([-10, -4, -2, -4, -2, 0]))  # -3
