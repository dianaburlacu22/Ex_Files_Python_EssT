from typing import List
import unittest

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique = 0

        for current in range(len(nums)):
            if nums[current] != val:
                nums[unique] = nums[current]
                unique += 1

            
        return unique
    

# Test cases
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [3,2,2,3]
        val = 3
        expected_val = 2
        expected = [2,2]
        print(f"Running test for nums = {nums}, val = {val}")
        result = self.solution.removeElement(nums, val)
        print(f"Expected result: {expected_val}, Actual result: {result}")
        self.assertEqual(result, expected_val)
        

    def test_example2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        expected_val = 5
        expected = [0,1,4,0,3]
        print(f"Running test for nums = {nums}, val = {val}")
        result = self.solution.removeElement(nums, val)
        print(f"Expected result: {expected_val}, Actual result: {result}")
        self.assertEqual(result, expected_val)


    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
