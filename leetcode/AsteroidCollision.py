"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 


"""

from typing import List
import unittest
from colorama import Fore, Style

class Solution:
    def asteroidCollision(self, asteroids: List[int]):
        
        resulting_asteroids = []

        for asteroid in range(len(asteroids) - 1):
            
                if asteroids[asteroid] > 0 and asteroids[asteroid + 1] > 0:
                    resulting_asteroids.append(asteroids[asteroid])
                elif asteroids[asteroid] == abs(asteroids[asteroid + 1]):
                        asteroid += 1
                elif asteroids[asteroid] > 0 and asteroids[asteroid + 1] < 0:
                    if abs(asteroids[asteroid]) < resulting_asteroids[-1]:
                        continue
                    elif asteroids[asteroid] > abs(asteroids[asteroid + 1]):
                        resulting_asteroids.append(asteroids[asteroid])
                    else:
                        resulting_asteroids.append(asteroids[asteroid + 1])
                    asteroid += 1

        return resulting_asteroids
    



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

        asteroids = [5,10,-5]
        expected = [5,10]

        # Call the merge method
        k = self.solution.asteroidCollision(asteroids)
        #Verify the merged array is as expected
        self.assertEqual(k, expected, Fore.RED + "The merged array did not match the expected one" + Style.RESET_ALL)

    def test_merge_example2(self):
        asteroids = [8,-8]
        expected = []

        k = self.solution.asteroidCollision(asteroids)
        self.assertEqual(k, expected, Fore.RED + "Failed on test case 2" + Style.RESET_ALL)

    def test_merge_example3(self):
        asteroids = [10,2,-5]
        expected = [10]

        k = self.solution.asteroidCollision(asteroids)
        self.assertEqual(k, expected, Fore.RED + "Failed on test case 3" + Style.RESET_ALL)


if __name__ == '__main__':
    print(Fore.CYAN + "Starting tests... \n" + Style.RESET_ALL)
    runner = CustomTestRunner(verbosity=2)
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestSolution))