# Write a function that takes a list of numbers and returns the maximum element.

def max_element(nums):

    max = nums[0]

    for num in nums:
        if num > max:
            max = num

    return max

# Test the function
print(max_element([1, 2, 3, 4]))  # Output: 4
print(max_element([5, 1, 9, 3]))  # Output: 9