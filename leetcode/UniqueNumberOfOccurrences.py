"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

"""

from typing import Counter, List
import unittest
from colorama import Fore, Style

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # 1. create a dictionary that counts the occurrences of each value
        # 2. extract the values from the occurrences and put it in an array
        # 3. convert the array to a set and compare their lenghts

        answer = False

        occurrences = Counter(arr)

        counts = list(occurrences.values())

        if len(counts) == len(set(counts)):
            answer = True

        return answer
    

# TESTS:
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
        arr = [1,2,2,1,1,3]

        expected = True

        # Call the merge method
        k = self.solution.uniqueOccurrences(arr)
        #Verify the merged array is as expected
        self.assertEqual(k, expected, Fore.RED + "The merged array did not match the expected one" + Style.RESET_ALL)

    def test_merge_example2(self):
        arr = [1, 2]

        expected = False
  
        k = self.solution.uniqueOccurrences(arr)
        self.assertEqual(k, expected, Fore.RED + "Failed on test case 2" + Style.RESET_ALL)

    def test_merge_example3(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
       
        expected = True
        
        k = self.solution.uniqueOccurrences(arr)
        self.assertEqual(k, expected, Fore.RED + "Failed on test case 3" + Style.RESET_ALL)

if __name__ == '__main__':
    print(Fore.CYAN + "Starting tests... \n" + Style.RESET_ALL)
    runner = CustomTestRunner(verbosity=2)
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestSolution))
