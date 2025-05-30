"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last index of each character seen
        char_index = {}
        max_length = 0
        left = 0  # Left pointer of the sliding window

        # Iterate over the string with right pointer
        for right, char in enumerate(s):
            # If the character is already in the dictionary and its index is within the current window
            if char in char_index and char_index[char] >= left:
                # Move the left pointer to the right of the last occurrence of the current character
                left = char_index[char] + 1
            # Update the last seen index of the current character
            char_index[char] = right
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
        return max_length
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring(""))
    print(solution.lengthOfLongestSubstring(" "))
    print(solution.lengthOfLongestSubstring("au"))
    print(solution.lengthOfLongestSubstring("dvdf"))
    print(solution.lengthOfLongestSubstring("abba"))
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    