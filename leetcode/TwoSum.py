from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            print(f"Current num: {num}, complement needed: {complement}")
            
            if complement in num_map:
                print(f"Found complement {complement} in num_map: {num_map}")
                return [num_map[complement], i]
            else:
                print(f"Adding num {num} to num_map with index {i}")
                num_map[num] = i
        
        return []

# Test cases
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        print(f"Running test for nums = {nums}, target = {target}")
        result = self.solution.twoSum(nums, target)
        print(f"Expected result: {expected}, Actual result: {result}")
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        print(f"Running test for nums = {nums}, target = {target}")
        result = self.solution.twoSum(nums, target)
        print(f"Expected result: {expected}, Actual result: {result}")
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        print(f"Running test for nums = {nums}, target = {target}")
        result = self.solution.twoSum(nums, target)
        print(f"Expected result: {expected}, Actual result: {result}")
        self.assertEqual(result, expected)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
