from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_ptr = 0
        
        for current_ptr in range(1, len(nums)):
            if nums[current_ptr] != nums[unique_ptr]:
                unique_ptr += 1
                nums[unique_ptr] = nums[current_ptr]
        
        # unique_ptr is zero-indexed, so the count of unique elements is unique_ptr + 1
        return unique_ptr + 1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1, 1, 2]
    expected1 = [1, 2]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == len(expected1)
    assert nums1[:k1] == expected1
    
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected2 = [0, 1, 2, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == len(expected2)
    assert nums2[:k2] == expected2
    
    print("All test cases passed!")
