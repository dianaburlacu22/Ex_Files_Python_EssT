from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Edge case handling, if the list is empty, return an empty string immediately
        if not strs:
            return ""
        
        # Initialize the prefix as the first string
        prefix = strs[0]
        
        # Helper function to find common prefix between two strings
        def commonPrefix(str1: str, str2: str) -> str:
            # Calculates the length of the shorter string between str1 and str2
            min_length = min(len(str1), len(str2))
            # Iterate through each character index from - to min_length -1
            for i in range(min_length):
                # If at any index i, the characters str1[i] and str2[i] are different, this means the common prefix ends before this index
                if str1[i] != str2[i]:
                    # Therefore this is returned as the longest common prefix
                    return str1[:i]
            # If the loop completes without finding any differing characters, this means one string is a prefix of the other or both strings are identical up to min_length. Thus, the entire prefix up to min_length is returned
            return str1[:min_length]
        
        # Compare the current prefix with each string in the array
        for s in strs[1:]:
            prefix = commonPrefix(prefix, s)
            if not prefix:
                break
        
        return prefix
    

