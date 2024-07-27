"""
55. Jump Game
Medium

Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

import unittest
from colorama import Fore, Style

class Solution:

    

class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.failed_tests = []

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed_tests.append(test)

    def addError(self, test, err):
        super().addError(test, err)
        self.failed_tests.append(test)

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        result = super().run(test)
        if result.failed_tests:
            print(Fore.RED + "Some tests failed: " + Style.RESET_ALL)
            for failed_test in result.failed_tests:
                print(Fore.RED + f" - {failed_test}" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "All tests are good!" + Style.RESET_ALL)
        return result
    
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_merge_example1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        expected = [1, 2, 2, 3, 5, 6]
        # Here we don't define a k because the function does not return anything
        # k = self.solution.merge(nums1, m, nums2, n)

        # Call the merge method
        self.solution.merge(nums1, m, nums2, n)
        #Verify the merged array is as expected
        self.assertEqual(nums1, expected, Fore.RED + "The merged array did not match the expected one" + Style.RESET_ALL)

    def test_merge_example2(self):
        nums1 = [1, 2, 4, 5, 6, 0]
        m = 5
        nums2 = [3]
        n = 1
        expected = [1, 2, 3, 4, 5, 6]
  
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected, Fore.RED + "Failed on test case 2" + Style.RESET_ALL)

    def test_merge_example3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected, Fore.RED + "Failed on test case 3" + Style.RESET_ALL)

if __name__ == '__main__':
    print(Fore.CYAN + "Starting tests... \n" + Style.RESET_ALL)
    runner = CustomTestRunner(verbosity=2)
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestSolution))