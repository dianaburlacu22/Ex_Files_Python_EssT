###
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
###

from typing import List
import unittest
from colorama import Fore, Style

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Initialise values
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        

# Example usage and test cases
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
