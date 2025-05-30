"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of opening brackets to their corresponding closing brackets
        bracket_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in bracket_map:
                # If it's an opening bracket, push the expected closing bracket onto the stack
                stack.append(bracket_map[char])
            else:
                # If it's a closing bracket, check if it matches the top of the stack
                if not stack or stack.pop() != char:
                    return False
        # If the stack is empty, all brackets matched correctly
        return not stack
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([)]"))
    print(solution.isValid("{[]}"))