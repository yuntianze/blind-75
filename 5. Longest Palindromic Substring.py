"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the string is empty or has only one character, it's itself a palindrome
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0  # Indices for the longest palindrome found
        
        def expand_from_center(left: int, right: int) -> (int, int):
            # Expand as long as the characters at left and right are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the indices of the palindrome substring
            return left + 1, right - 1
        
        for i in range(len(s)):
            # Odd length palindrome (center at i)
            l1, r1 = expand_from_center(i, i)
            # Even length palindrome (center between i and i+1)
            l2, r2 = expand_from_center(i, i + 1)
            # Update the result if a longer palindrome is found
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        # Return the longest palindromic substring
        return s[start:end+1]
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("cbbd"))
    print(solution.longestPalindrome("a"))
    print(solution.longestPalindrome("ac"))
    print(solution.longestPalindrome("abba"))
    print(solution.longestPalindrome("dabbbabbbac"))