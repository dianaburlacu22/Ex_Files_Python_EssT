"""
1657. Determine if Two Strings Are Close
Medium

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
"""
import unittest
from colorama import Fore, Style
from typing import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        answer = True

        # 1. Check the lenghts of the strings. If different, return False immediately
        if len(word1) != len(word2):
            return False
        
        # 2. Check if the unique characters are the same in both words
        # If they are different, then the swap cannot be made
        if set(word1) != set(word2):
            return False
        
        # 3. Check if the occurrences of each character is the same in both words
        if sorted(Counter(word1).values()) != sorted(Counter(word2).values()):
            return False


        return answer




### TESTS
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
        word1 = "abc"
        word2 = "bca"
        expected = True

        # Here we don't define a k because the function does not return anything
        # k = self.solution.merge(nums1, m, nums2, n)

        # Call the merge method
        k = self.solution.closeStrings(word1, word2)
        #Verify the merged array is as expected
        self.assertEqual(k, expected, Fore.RED + "The merged array did not match the expected one" + Style.RESET_ALL)

    def test_merge_example2(self):
        word1 = "a"
        word2 = "aa"
        expected = False

        k = self.solution.closeStrings(word1, word2)
        self.assertEqual(k, expected, Fore.RED + "Failed on test case 2" + Style.RESET_ALL)

    def test_merge_example3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        expected = True
        
        k = self.solution.closeStrings(word1, word2)
        self.assertEqual(k, expected, Fore.RED + "Failed on test case 3" + Style.RESET_ALL)

if __name__ == '__main__':
    print(Fore.CYAN + "Starting tests... \n" + Style.RESET_ALL)
    runner = CustomTestRunner(verbosity=2)
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestSolution))