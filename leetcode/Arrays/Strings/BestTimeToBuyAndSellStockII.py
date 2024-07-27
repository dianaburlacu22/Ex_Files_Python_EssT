"""
122. Best Time to Buy and Sell Stock II
Medium

Topics
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
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