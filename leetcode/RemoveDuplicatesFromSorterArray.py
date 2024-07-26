from typing import List
import unittest
from colorama import Fore, Style

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

    def test_removeDuplicates_example1(self):
        nums = [1, 1, 2]
        expected = [1, 2]
        # Defining k because the function returns something
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, len(expected), Fore.RED + "Failed on test case 1: Length mismatch." + Style.RESET_ALL)
        self.assertEqual(nums[:k], expected, Fore.RED + "Failed on test case 1: Array content mismatch." + Style.RESET_ALL)

    def test_removeDuplicates_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, len(expected), Fore.RED + "Failed on test case 2: Length mismatch." + Style.RESET_ALL)
        self.assertEqual(nums[:k], expected, Fore.RED + "Failed on test case 2: Array content mismatch." + Style.RESET_ALL)

if __name__ == '__main__':
    print(Fore.CYAN + "Starting tests... \n" + Style.RESET_ALL)
    runner = CustomTestRunner(verbosity=2)
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestSolution))